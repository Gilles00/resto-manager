﻿from django.contrib.auth.models import User
from django.forms import ModelForm
from restaurants.models import Restaurant
from comptes.models import Restaurateur
from django import forms
from django.contrib.auth.hashers import make_password
from django.template.defaultfilters import stringfilter
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db.models import Q
from django.core.mail import EmailMessage

class CreateRestaurateurForm(forms.Form):
    error_messages = {
		'duplicate_username': ("Un utilisateur avec ce nom d'utilisateur existe déjà."),
    }

    first_name = forms.CharField(
        label=("Prénom")
    )

    last_name = forms.CharField(
        label=("Nom")
    )
	
    username = forms.EmailField(
        label=("Courriel")
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

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username']
        )

    def save(self, commit=True):
        temp_password = User.objects.make_random_password()
        email = self.cleaned_data["username"]
	
        user_data = User(
            username = email,
            first_name = self.cleaned_data["first_name"],
            last_name = self.cleaned_data["last_name"]
        )
		
        user_data.set_password(temp_password)
		
        restaurateur = Restaurateur()
        restaurateur.telephone = self.cleaned_data["telephone"]
        #Avant de sauvegarder le user, on veut s'assurer que le profile du restaurateur est correct
        restaurateur.full_clean()
		
        user_data.save()
        restaurateur.user = user_data
        restaurateur.save()
		
        full_name = user_data.first_name + " " + user_data.last_name
        self.send_confirmation_email(restaurateur, temp_password)

        return restaurateur
		
    def send_confirmation_email(self, restaurateur, temp_password):
        title = "Confirmation d'inscription"

        full_name = restaurateur.user.first_name + " " + restaurateur.user.last_name
		
        warning = ""
		
        content = """
<div>Bienvenue sur Resto Manager, {0}!</div>
<br />

<div>Voici les informations que vous devez utiliser pour vous connecter:<br />
Courriel: {1}<br />
Mot de passe: {2}</div>
<div>
<br />

<a href="http://localhost">Cliquez ici pour commencer</a></div>
<br />

{3}
		""".format(full_name, restaurateur.user.username, temp_password, warning)

        from_email = "etsrestomanager@gmail.com"
        to_emails = [restaurateur.user.username]

        msg = EmailMessage(title, content, from_email, to_emails)
        msg.content_subtype = "html"
        msg.send()

#Formulaire pour un admin souhaitant modifier les informations d'un restaurateur
class EditRestaurateurForm(ModelForm):
    first_name = forms.CharField(
        label=("Prénom"),
        widget=forms.TextInput
    )
	
    last_name = forms.CharField(
        label=("Nom"),
        widget=forms.TextInput
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
	
    class Meta:
        model = ''
		
    def save(self, commit=True):
        restaurateur = self.instance
        user_data = restaurateur.user

        user_data.first_name = self.cleaned_data["first_name"]
        user_data.last_name = self.cleaned_data["last_name"]
        restaurateur.telephone = self.cleaned_data["telephone"]
		
        #Avant de sauvegarder le user, on veut s'assurer que le profile du restaurateur est correct
        restaurateur.full_clean()
		
        user_data.save()
        restaurateur.save()

        return restaurateur

    def __init__(self, *args, **kwargs):
        super(EditRestaurateurForm, self).__init__(*args,**kwargs)
		
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['telephone'].initial = self.instance.telephone
		
#Formulaire pour un restaurateur souhaitant modifier ses informations
class SelfEditRestaurateurForm(ModelForm):
    error_messages = {
        'password_error': ("Les mots de passe entrés ne correspondent pas."),
    }
	
    first_name = forms.CharField(
        label=("Prénom"),
        widget=forms.TextInput
    )
	
    last_name = forms.CharField(
        label=("Nom"),
        widget=forms.TextInput
    )

    telephone = forms.CharField(
        label=("Téléphone"),
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^([0-9]|\-)+$',
                message='Format invalide. Le numéro de téléphone ne doit contenir que des chiffres et des tirets (-).',
                code='invalid_phone'
            ),
        ]
    )

    password = forms.CharField(
        label=("Nouveau mot de passe"),
        widget=forms.PasswordInput,
        required=False
    )

    password2 = forms.CharField(
        label=("Réentrez le mot de passe"),
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = ''

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password != password2:
            raise forms.ValidationError(
                self.error_messages['password_error'],
            )
        return password2

    def save(self, commit=True):
        restaurateur = self.instance
        user_data = restaurateur.user

        user_data.first_name = self.cleaned_data["first_name"]
        user_data.last_name = self.cleaned_data["last_name"]
        restaurateur.telephone = self.cleaned_data["telephone"]
		
        #Si l'utilisateur n'entre pas de mot de passe, il ne veut pas le changer
        if self.cleaned_data["password"].strip():
            user_data.password = make_password(self.cleaned_data["password"].strip())
            user_data.save()
		
        #Avant de sauvegarder le user, on veut s'assurer que le profile du restaurateur est correct
        restaurateur.full_clean()
		
        user_data.save()
        restaurateur.save()

        return restaurateur

    def __init__(self, *args, **kwargs):
        super(SelfEditRestaurateurForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['telephone'].initial = self.instance.telephone