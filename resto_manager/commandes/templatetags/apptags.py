# Pour les dictionnaires dans les templates
from django import template
from django.template.defaultfilters import stringfilter
from restaurants.models import Restaurant, Menu, Repas

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
	
@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return qty * unit_price
	
@register.filter
@stringfilter
def int_to_string(value):
    return str(value)
	
@register.filter
def get_repas_list(restaurant_id):
    repas = Menu.objects.get(restaurant_id = restaurant_id).repas.all()
    # you would need to do any localization of the result here
    return repas