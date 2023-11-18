import datetime as dt
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from django.db.models import Q
from accounts import models as m
from . import forms
from img_study_buddy.utils import meeting

# Create your views here.

@login_required
def create_a_meeting(request,requested_id):
    template_name = 'create_a_meeting.html'
    form = forms.MeetingForm(request.POST or None)
    requested = get_object_or_404(m.User,id=requested_id)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.requester = request.user
            new_form.requested =requested
            new_form.save()
            messages.success(request,'Meeting request sent to {}'.format(requested.get_full_name()))
            return redirect('accounts:public_profile',requested_id)  
    context ={
        'form':form,
        'requested':requested
    }
    return render(request, template_name,context)


@login_required
def reject_accept_or_cancel_a_meeting(request,meeting_id,type):
    url = request.META.get('HTTP_REFERER')
    requested = request.user
    was_meeting_accepted = None
    was_meeting_cancelled = None
    was_meeting_rejected = None
    obj = get_object_or_404(models.Meeting, id=meeting_id)
    if obj.requested is not None:
        requested = obj.requested
    if type == 'accepted':
        was_meeting_accepted = True
    elif type == 'rejected':
        was_meeting_rejected = True
    else:
        was_meeting_cancelled = True
    obj.was_meeting_accepted = was_meeting_accepted
    obj.was_meeting_cancelled = was_meeting_cancelled
    obj.was_meeting_rejected = was_meeting_rejected
    obj.requested = requested
    obj.save()
    messages.success(request,'Meeting was successfully {}'.format(type))
    return redirect(url)

@login_required
def reschedule_a_meeting(request, meeting_id):
    template_name = 'reschedule_a_meeting.html'
    msg ='Meeting reschedule'
    meeting_obj = get_object_or_404(models.Meeting,id=meeting_id)
    if request.method == 'POST':
        form = forms.MeetingForm(request.POST, instance=meeting_obj)
        if form.is_valid():
            date  = request.POST.get('date')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            requester = meeting_obj.requester.get_full_name()
            receipient = meeting_obj.requested.username()
            meeting_obj.save()
            #sent a meeting resheduled
            meeting(msg,requester, date, start_time, end_time,[receipient,])
            messages.success(request,'Meeting successfully rescheduled')
    form = forms.MeetingForm(instance=meeting_obj)
    return render(request,template_name,{"obj":meeting_obj,"form":form})


@login_required
def was_attended(request,meeting_id, status):
    url = request.META.get('HTTP_REFERER')
    attendence = ''
    if status == 'yes':
        attendence = True
    else:
        attendence = False
    meeting_obj = get_object_or_404(models.Meeting,id=meeting_id)
    meeting_obj.was_meeting_attended = attendence
    meeting_obj.save()
    messages.success(request,'Status successfully updated.')
    return redirect(url)

@login_required
def meetings(request):
    template_name = 'meetings.html'
    user =  request.user
    date_today = dt.date.today()
    meetings_qs = models.Meeting.objects.filter(requested = user)
    incoming_meetings = meetings_qs.filter(was_meeting_accepted = None).filter(was_meeting_attended=None).filter(was_meeting_cancelled = None).filter(was_meeting_rejected=None).filter(date__gte = date_today)
    outgoing_meetings = models.Meeting.objects.filter(requester = user).filter(was_meeting_accepted = None).filter(was_meeting_attended=None).filter(was_meeting_cancelled = None).filter(was_meeting_rejected=None).filter(date__gte = date_today)
    upcoming_meetings =  models.Meeting.objects.filter(Q(requester = user) | Q(requested=user)).filter(was_meeting_accepted=True).filter(was_meeting_attended=None).filter(was_meeting_cancelled = None).filter(was_meeting_rejected=None).filter(date__gte = date_today)
    past_meetings = meetings_qs.filter(was_meeting_attended=True).filter(was_meeting_accepted = True).filter(was_meeting_cancelled = None).filter(was_meeting_rejected=None).filter(date__lt = date_today).filter(requester = user)
    reject_meetings = models.Meeting.objects.filter(Q(requester = user) | Q(requested=user)).filter(date__gte=date_today).filter(was_meeting_rejected=True)
    brodcast_meeting = models.Meeting.objects.filter(requested = None).filter(was_meeting_accepted = None).filter(was_meeting_attended=None).filter(was_meeting_cancelled = None).filter(was_meeting_rejected=None).filter(date__gt = date_today).exclude(requester=user)
    form  = forms.MeetingForm(request.POST or None)
    context = {
        "upcoming_meetings": upcoming_meetings,
        "incoming_meetings" : incoming_meetings,
        "outgoing_meetings": outgoing_meetings,
        "past_meetings":past_meetings,
        "brodcast_meetings":brodcast_meeting,
        "reject_meetings":reject_meetings,
        "form":form
    }
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.requester = request.user
            new_form.save()
            messages.success(request,'Meeting was successfully broadcasted.')
    return render(request,template_name, context)

@login_required
def check_if_meeting_occured(request):
    template_name = 'check_if_meeting_occured.html'
    #meeting was excepted
    #due date has passed 
    #was attended is null
    #request should verify if meeting was attended
    date_today = dt.date.today()
    meetings_qs = models.Meeting.objects.filter(requester = request.user).filter(was_meeting_accepted=True).filter(was_meeting_attended = None).filter(date__lt = date_today)
    return render(request,template_name,{'meetings':meetings_qs})

@login_required
def coach_meeting_board(request):
    template_name = 'coach_meeting_board.html'
    # requested meetings that are still valid 1.date hasnt passed
    # past meetings that were attended 1. accepted == true 2. attended == true 3. date has passed
    # upcoming meetings 1.date hasnt passed 2.accepted == teue
    form  = forms.MeetingForm()
    date_today = dt.date.today()
    meetings_qs = models.Meeting.objects.filter(requested = request.user)
    print('meetings_qs')
    print(meetings_qs)
    reject_meetings = meetings_qs.filter(date__gte=date_today).filter(was_meeting_rejected=True)
    upcoming_meetings = meetings_qs.filter(date__gte=date_today).filter(was_meeting_accepted=True)
    requested_meetings = meetings_qs.filter(date__gte=date_today).filter(was_meeting_accepted = None)
    past_meetings = meetings_qs.filter(was_meeting_accepted = True).filter(was_meeting_attended = True).filter(date__lt=date_today)
    context = {
        'upcoming_meetings':upcoming_meetings,
        'incoming_meetings':requested_meetings,
        'past_meetings':past_meetings,
        'reject_meetings':reject_meetings,
        'form':form

    } 
    return render(request,template_name,context)

@login_required
def all_meetings_admin(request):
    template_name = 'meetings_admin.html'
    meetings =  models.Meeting.objects.all()
    return render(request,template_name,{'meetings':meetings})


