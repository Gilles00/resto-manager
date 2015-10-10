# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.forms import ModelForm
from restaurants.models import Restaurant
from comptes.models import Restaurateur
from django import forms
from django.template.defaultfilters import stringfilter
from django.core.validators import RegexValidator

class CreateRestaurantForm(forms.Form):
    error_messages = {
		'duplicate_name': ("Un restaurant avec ce nom existe déjà."),
    }

    nom = forms.CharField(
        label=("Nom")
    )
	
    adresse = forms.CharField(
        label=("Adresse")
    )

    telephone = forms.CharField(
        label=("Téléphone"),
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^([0-9]|\-)+$',
                message = 'Format invalide. Le numéro de téléphone ne doit contenir que des chiffres et des tirets (-).',
                code='invalid_phone'
            ),
            ]
    )

    restaurateur = forms.ModelChoiceField(
        label=("Restaurateur"),
        queryset=Restaurateur.objects.all(),
        required=False
    )

    def clean_nom(self):
        nom = self.cleaned_data["nom"]

        try:
            Restaurant._default_manager.get(nom=nom)
        except Restaurant.DoesNotExist:
            return nom
        raise forms.ValidationError(
            self.error_messages['duplicate_name']
        )

    def save(self, commit=True):
        restaurant = Restaurant()
		
        restaurant.nom = self.cleaned_data["nom"]
        restaurant.adresse = self.cleaned_data["adresse"]
        restaurant.telephone = self.cleaned_data["telephone"]
        restaurant.restaurateur = self.cleaned_data["restaurateur"]
		
        restaurant.save()

        return restaurant

class EditRestaurantForm(ModelForm):
    adresse = forms.CharField(
        label=("Adresse")
    )
	
    telephone = forms.CharField(
        label=("Téléphone"),
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^([0-9]|\-)+$',
                message = 'Format invalide. Le numéro de téléphone ne doit contenir que des chiffres et des tirets (-).',
                code='invalid_phone'
            ),
            ]
    )

    restaurateur = forms.ModelChoiceField(
        label=("Restaurateur"),
        queryset=Restaurateur.objects.all(),
		required=False
    )
	
    class Meta:
        model = ''
		
    def save(self, commit=True):
        restaurant = self.instance

        restaurant.adresse = self.cleaned_data["adresse"]
        restaurant.telephone = self.cleaned_data["telephone"]
        restaurant.restaurateur = self.cleaned_data["restaurateur"]
		
        restaurant.save()

        return restaurant

    def __init__(self, *args, **kwargs):
        super(EditRestaurantForm, self).__init__(*args,**kwargs)
        self.fields['adresse'].initial = self.instance.adresse
        self.fields['telephone'].initial = self.instance.telephone
        self.fields['restaurateur'].initial = self.instance.restaurateur