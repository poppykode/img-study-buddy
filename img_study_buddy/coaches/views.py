import pytz
from django.db.models import Q
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.core.paginator import Paginator
from img_study_buddy.utils import (
    pagination_qs,
)

@login_required
def view_all_coaches(request):
    template_name = 'view_all_coaches.html'
    # coaches_qs =  User.objects.filter(is_coach = True,is_registration_complete=True,is_coach_accepted=True).exclude(id=request.user.id)
    coaches_qs =  User.objects.filter(is_coach = True,is_registration_complete=True).exclude(id=request.user.id)
    final_qs = ''
    time_zones = pytz.all_timezones_set
    if request.method== 'POST':
        time_zone = request.POST.get('time_zone_')
        avg_rating = request.POST.get('avg_rating')
        budget = request.POST.get('budget')
        if time_zone == '':
            time_zone = None
        if avg_rating == '':
            avg_rating = None
        if budget == '':
            budget = None
        final_qs= coaches_qs.filter(
            Q(user_avg_rating =avg_rating)|
            Q (user_general_additional_info__time_zone=time_zone)|
            Q(user_coach_additional_info__rate=budget)
        )
        context = {
            'obj':pagination_qs(request,final_qs),
            'coaches':len(final_qs),
            'time_zones':time_zones,
            'time_zone':time_zone,
            'budget':budget,
            'avg_rating': avg_rating,
            'type':1
        }

        return render(request,template_name,context)
    final_qs = coaches_qs
    context = {
        'obj':pagination_qs(request,final_qs),
        'coaches':len(final_qs),
        'time_zones':time_zones,
        'time_zone':'',
        'budget':'',
        'avg_rating': '',
        'type':2
    }
    return render(request,template_name,context)