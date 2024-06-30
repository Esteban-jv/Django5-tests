from django import template

register = template.Library()

@register.simple_tag(name="registers_number")
def registers_number(paginator):
    print (paginator.count)
    return f"{paginator.count} registers found"

@register.filter(name="some_custom_filter")
def name(value):
    return f"José Esteban {value}"