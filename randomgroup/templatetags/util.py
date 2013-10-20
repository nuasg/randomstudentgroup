import random
import string
from django import template

register = template.Library()
hex_letter = string.hexdigits[:-6]

@register.simple_tag
def random_color():
    color = ''
    for i in range(6):
        color += random.choice(hex_letter)
    print color
    return '#%s' % color
