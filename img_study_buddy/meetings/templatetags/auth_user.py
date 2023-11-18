from django import template
from django.shortcuts import get_object_or_404
from accounts.models import  User

register = template.Library()

@register.filter(name='reliability')
def get_reliability(user_id):
    user = get_object_or_404(User,id=user_id)
    reliability = user.reliability()
    return reliability

@register.filter(name='meetings_attended')
def get_meetings_attended(user_id):
    user = get_object_or_404(User,id=user_id)
    meetings_attended = user.meetings_attended()
    return meetings_attended





