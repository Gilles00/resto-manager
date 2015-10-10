#!/usr/bin/python
# -*- coding: utf-8 -*-

from forms import LoginForm
from forms import UserForm
from forms import EditUserForm

from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login

def index(request):
    if request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        return login_user(request)

def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Vous avez été connecté avec succès.")

                    """On utilise un HttpResponseRedirect car on ne veut pas répéter
                    la connection qui s'est effectuée avec succès si la page est rafraîchit"""
                    return HttpResponseRedirect("/")
                else:
                    messages.error(request, "Votre compte n'est pas activé.")
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_user(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/comptes/login")

    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return HttpResponseRedirect("/")

def create_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            birthdate = form.cleaned_data.get("birthdate")
            address = form.cleaned_data.get("address")
            telephone = form.cleaned_data.get("telephone")
            password = form.cleaned_data.get("password")

            new_user = authenticate(username=username, password=password)
            login(request, new_user)

            message_connection = """Merci de vous être enregistré.
									Voici les informations saisies:"""

            messages.success(request, message_connection)

            messages.info(request, "Courriel: " + username)
            messages.info(request, "Nom complet: " + first_name + " " + last_name)
            messages.info(request, "Date de naissance: " + str(birthdate))
            messages.info(request, "Adresse: " + address)
            messages.info(request, u"Numéro de téléphone: " + telephone)

            return HttpResponseRedirect("/")
    else:
        form = UserForm()

    return render(request, 'createuser.html', {'form': form})

def manage_user(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/comptes/login")

    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            address = form.cleaned_data.get("address")
            telephone = form.cleaned_data.get("telephone")

            message_connection = """Vos informations ont été sauvegardées.
									Voici les informations saisies:"""

            messages.success(request, message_connection)

            messages.info(request, "Adresse: " + address)
            messages.info(request, u"Numéro de téléphone: " + telephone)

            return HttpResponseRedirect('/comptes/manage')
    else:
        form = EditUserForm(instance=request.user)

    return render(request, 'manageuser.html', {'form': form })
