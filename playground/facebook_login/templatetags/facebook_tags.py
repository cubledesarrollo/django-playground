'''
Created on 08/04/2013

@author: Cuble Desarrollo
'''
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def facebook_i18n(value):
    """ Adapta el LANGUAGE_CODE para poder ser usado en el snipet de JavaScript
    que se usa para Facebook Login. """
    if value == 'en':
        return 'en_US'
    if value == 'es':
        return 'es_ES'
    return value
