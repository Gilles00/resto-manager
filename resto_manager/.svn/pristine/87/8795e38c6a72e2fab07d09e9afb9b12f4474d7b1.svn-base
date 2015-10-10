#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import reversion

class Livreur(models.Model):
    user = models.OneToOneField(User, related_name="livreur", null=True, blank=True)
    telephone = models.CharField(max_length=20,null=True,blank=True)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name
	
    def delete(self):
        #En supprimant le user associé, le livreur est automatiquement supprimé ON CASCADE
        self.user.delete()
		
#Pour le undo
reversion.register(Livreur)