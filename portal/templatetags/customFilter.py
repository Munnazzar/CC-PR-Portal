from django import template
register = template.Library()

@register.filter
def getItem(dictionary, key):
    return dictionary.get(key)