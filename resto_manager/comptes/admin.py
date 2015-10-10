from django.contrib import admin
from comptes.models import Restaurateur
from comptes.models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.

class RestaurateurAdmin(admin.ModelAdmin):
    pass

admin.site.register(Restaurateur)
admin.site.register(UserProfile)


#admin.site.unregister(User)
#admin.site.unregister(Group)
