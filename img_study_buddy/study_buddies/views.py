import pytz
from django.db.models import Q
from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.core.paginator import Paginator
from img_study_buddy.utils import (
    pagination_qs,
)

# Create your views here.
@login_required
def view_all_study_buddies(request):
    template_name = 'view_all_study_buddies.html'
    candidates_qs =  User.objects.filter(is_candidate = True,is_registration_complete=True).exclude(id=request.user.id)
    final_qs = ''
    time_zones = pytz.all_timezones_set

    if request.method== 'POST':
        time_zone = request.POST.get('time_zone_')
        exam_date = request.POST.get('exam_date')
        availability = request.POST.get('availability')
        online_offline = request.POST.get('online_offline')
        if time_zone == '':
            time_zone = None
        if exam_date == '':
            exam_date = None
        if online_offline == '':
            online_offline = None
        if availability == '':
            availability = None
        print('____')
        print(time_zone)
        final_qs= candidates_qs.filter(
            Q(user_candidate_additional_info__availability =availability)|
            Q (user_general_additional_info__time_zone=time_zone)|
            Q(user_candidate_additional_info__exam_date=exam_date)
            )
        context = {
            'obj':pagination_qs(request,final_qs),
            'candidates':len(final_qs),
            'time_zones':time_zones,
            'time_zone':time_zone,
            'exam_date':exam_date,
            'availability': availability,
            'online_offline': online_offline,
            'type':1
        }

        return render(request,template_name,context)
    final_qs = candidates_qs
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
