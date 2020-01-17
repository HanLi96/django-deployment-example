from django import template

register = template.Library()

def cut(value, arg):
    """
    cuts out all values of arg from the string
    """

    return value.replace(arg,'')

# fist is the string you call the filter, second is the filter functioin
register.filter('cut',cut)
