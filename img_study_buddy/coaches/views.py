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
    coaches_qs =  User.objects.filter(is_coach = True,is_registration_complete=True).exclude(id=request.user.id)
    final_qs = ''
    time_zones = pytz.all_timezones_set
    if request.method== 'POST':
        time_zone = request.POST.get('time_zone_')
        ratings = request.POST.get('ratings')
        budget = request.POST.get('budget')
        if time_zone == '':
            time_zone = None
        if ratings == '':
            ratings = None
        if budget == '':
            budget = None
        final_qs= coaches_qs.filter(
            Q(user_rated_review__rating =ratings)|
            Q (user_general_additional_info__time_zone=time_zone)|
            Q(user_coach_additional_info__=budget)
        )
        context = {
            'obj':pagination_qs(request,final_qs),
            'candidates':len(final_qs),
            'time_zones':time_zones,
            'time_zone':time_zone,
            'budget':budget,
            'ratings': ratings,
            'type':1
        }

        return render(request,template_name,context)
    final_qs = coaches_qs
    context = {
        'obj':pagination_qs(request,final_qs),
        'candidates':len(final_qs),
        'time_zones':time_zones,
        'time_zone':'',
        'exam_date':'',
        'availability':'',
        'online_offline':'',
        'type':2
    }
    return render(request,template_name,context)