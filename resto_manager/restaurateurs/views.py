# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from comptes.models import Restaurateur
from restaurants.models import Restaurant
from forms import CreateRestaurateurForm
from forms import EditRestaurateurForm
from forms import SelfEditRestaurateurForm
from django.core import serializers
from django.contrib import messages

import reversion
from reversion.models import Revision

def show_restaurateurs(request):
    if request.user.is_authenticated() and request.user.is_superuser == True:
        restaurateurs = Restaurateur.objects.all()
	
        return render(request, 'restaurateurs_list.html', {'restaurateurs': restaurateurs})
    else:
        return HttpResponseRedirect("/comptes/login")

@reversion.create_revision()
def add_restaurateur(request):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect("/comptes/login")

    availables = Restaurant.objects.filter(restaurateur=None).all()
		
    if request.method == "POST":
        form = CreateRestaurateurForm(request.POST)
        if form.is_valid():
            #On ne veut pas pouvoir undo les items supprimés avant cet ajout
            clear_deleted_restaurateurs(request)
            restaurateur = form.save()
            
            for restaurant_id in request.POST.getlist('restaurants'):
                restaurant = Restaurant.objects.get(id=restaurant_id)
                restaurateur.restaurants.add(restaurant)
			
            no_restaurant = "false"
			
            if restaurateur.restaurants.count() == 0:
                no_restaurant = "true"
			
            return HttpResponse('{"success": true, "noRestaurant": ' + no_restaurant + ', "id": ' + str(restaurateur.id) + '}')
    else:
        form = CreateRestaurateurForm()

    return render(request, 'create_restaurateur.html', {'form': form, 'availables': availables})

@reversion.create_revision()
def delete_restaurateur(request, restaurateur_id):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect("/comptes/login")

    #On ne peut que undo le dernier restaurateur supprimé, donc on vide les backups avant de supprimer
    clear_deleted_restaurateurs(request)
		
    restaurateur = Restaurateur.objects.get(pk=restaurateur_id)
	
    #On ne veut pas supprimer un restaurant lorsqu'on supprime un restaurateur,
    #mais on veut également pouvoir faire un undo par la suite
	
    for restaurant in restaurateur.restaurants.all():
        restaurant.restaurateur = None
        restaurant.save()
	
    restaurateur.delete()

    return HttpResponse("success")

@reversion.create_revision()
def edit_restaurateur(request, restaurateur_id):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect("/comptes/login")

    restaurateur = Restaurateur.objects.get(pk=restaurateur_id)
    restaurants = restaurateur.restaurants.all()
    availables = Restaurant.objects.filter(restaurateur=None).all()
	
    if request.method == "POST":
        form = EditRestaurateurForm(request.POST, instance=restaurateur)
        if form.is_valid():
            #On ne veut pas pouvoir undo les items supprimés avant cette modification
            clear_deleted_restaurateurs(request)
            restaurateur = form.save()
			
            restaurateur.restaurants.clear()
			
            for restaurant_id in request.POST.getlist('restaurants'):
                restaurant = Restaurant.objects.get(id=restaurant_id)
                restaurateur.restaurants.add(restaurant)
				
            no_restaurant = "false"
			
            if restaurateur.restaurants.count() == 0:
                no_restaurant = "true"
			
            return HttpResponse('{"success": true, "noRestaurant": ' + no_restaurant + ', "id": ' + str(restaurateur.id) + '}')
    else:
        form = EditRestaurateurForm(instance=restaurateur)

    return render(request, 'edit_restaurateur.html', {'form': form, 'restaurants': restaurants, 'availables': availables})

def get_restaurateur(request, restaurateur_id):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect("/comptes/login")
    
    restaurateur = Restaurateur.objects.get(pk=restaurateur_id)

    return render(request, 'restaurateur_row.html', {'restaurateur': restaurateur})

def undo_last_delete(request):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect("/comptes/login")

    delete_list = reversion.get_deleted(Restaurateur)

    if delete_list:
        # Temporary, à convertir pour liste éventuellement
        restaurateurId = delete_list[0].object_id
        delete_version = delete_list.latest('revision')
        delete_version.revision.revert()

        return HttpResponse('{"success": true, "id": ' + str(restaurateurId) + '}')

def clear_deleted_restaurateurs(request):
    if not request.user.is_authenticated() or not request.user.is_superuser:
        return HttpResponseRedirect("/comptes/login")
		
    deleted_revisions = reversion.get_deleted(Restaurateur).select_related('revision')
    
    for deleted_revision in deleted_revisions:
        Revision.objects.filter(id=deleted_revision.revision_id).delete()

#Fonction appelée lorsqu'un restaurateur veut modifier ses propres informations
def self_edit_restaurateur(request):
    #On permet seulement aux restaurateurs d'accéder à la page
    if not request.user.is_authenticated() or not request.user.restaurateur:
        return HttpResponseRedirect("/comptes/login")

    if request.method == "POST":
        form = SelfEditRestaurateurForm(request.POST, instance=request.user.restaurateur)
        if form.is_valid():
            form.save()

            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            telephone = form.cleaned_data.get("telephone")

            message_connection = """Vos informations ont été sauvegardées.
									Voici les informations saisies:"""

            messages.success(request, message_connection)

            messages.info(request, u"Prénom: " + first_name)
            messages.info(request, "Nom: " + last_name)
            messages.info(request, u"Numéro de téléphone: " + telephone)

            return HttpResponseRedirect('/restaurateurs/manage')
    else:
        form = SelfEditRestaurateurForm(instance=request.user.restaurateur)

    return render(request, 'self_edit_restaurateur.html', {'form': form })