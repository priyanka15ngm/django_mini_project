from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def upper(value):
    if ',' in value:
        return value.split(',')[0].upper() + ' AGO'
    else:
        return value.upper()


upper.is_safe = True
