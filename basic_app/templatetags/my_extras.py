from django import template

register = template.Library()

@register.filter(name='cut') 

def cut(value,arg):
    # This cut "arg" from value
    return value.replace(arg,'')

#register.filter('cut',cut)
