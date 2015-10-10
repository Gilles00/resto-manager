from django.db import models
from django import forms


# Create your models here.


#from django.core.mail import EmailMessage

#email = EmailMessage('Hello', 'World', to=['etsrestomanager@gmail.com'])

#email.send()

#1

#class NameForm(forms.Form):
 #   your_name = forms.CharField(label='Your name', max_length=100)

class Notification(forms.Form):
    destinataire = forms.CharField(label='Destinataire',max_length=120)
    sujet = forms.CharField(label='Sujet', max_length=120)
    contenu = forms.CharField(label='Contenu', max_length=255)

