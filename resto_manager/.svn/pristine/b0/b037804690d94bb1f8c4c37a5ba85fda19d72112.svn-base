from django.db import models
from restaurants.models import Repas, Restaurant
from comptes.models import UserProfile
from livreurs.models import Livreur

class Commande(models.Model):
	client = models.ForeignKey(UserProfile, related_name='commandes')
	livreur = models.ForeignKey(Livreur, related_name='commandes', null=True)
	restaurant = models.ForeignKey(Restaurant, related_name='commandes')
	state = models.CharField(max_length=50)
	prix_total = models.DecimalField(max_digits=20, decimal_places=2, null=True)
	date = models.DateField(auto_now_add=True, null=True)
	date_acceptee = models.DateField(null=True)
	adresse = models.CharField(max_length=50, null=True)
	date_livraison = models.DateField(null=True)
	heure_livraison = models.TimeField(null=True)

class LigneCommande(models.Model):
	commande = models.ForeignKey(Commande, related_name='ligne_commandes')
	repas = models.ForeignKey(Repas, related_name='ligne_commandes')
	prix = models.DecimalField(max_digits=20, decimal_places=2)
	quantity = models.IntegerField()