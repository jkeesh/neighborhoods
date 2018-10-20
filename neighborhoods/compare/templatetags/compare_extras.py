from django import template

from compare.views import get_best_match

register = template.Library()

@register.simple_tag
def best_match(city1, city2, neighborhood1):
    """Return the best match template tag helper"""
    return get_best_match(city1, city2, neighborhood1)

