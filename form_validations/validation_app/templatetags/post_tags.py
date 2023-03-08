from django import template
from .. models import Student
# creating customized template tags using 'simple_tag'

register = template.Library()

@register.simple_tag
def total():
    return Student.objects.count()