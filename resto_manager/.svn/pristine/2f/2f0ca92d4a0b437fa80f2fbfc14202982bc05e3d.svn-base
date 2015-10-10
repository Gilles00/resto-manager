from django import forms
from django.db import models


choixTypeUnite = (
    ('metrique', 'Metrique'),
    ('imperial', 'Impérial'),
)
  
class DirectionForm(forms.Form):
    Origine = forms.CharField(label='Your name', max_length=100)
    Destination = forms.CharField(label='Your name', max_length=100)
    Unite = forms.CharField(label='Choix d\'unité', choices=choixTypeUnite,
                            default='metrique', max_length=100)
