from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='is_member')
def is_member(user):
    return user.groups.filter(name='Member').exists()