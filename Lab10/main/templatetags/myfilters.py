from django import template

register = template.Library()

@register.filter(name='range')
def filter_range(x):
    return range(x)
