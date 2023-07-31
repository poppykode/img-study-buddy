import datetime as dt
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from accounts import models as m
from . import forms

# Create your views here.

@login_required
def create_a_meeting(request,requested_id=None):
    url = request.META.get('HTTP_REFERER')
    msg = 'Meeting request was broadcasted.'
    if request.method == 'POST':
        requested = None
        if not requested_id == None:
            requested = get_object_or_404(m.User,id=requested_id)
            msg = 'Meeting request sent to {}'.format(requested.get_full_name())
        models.Meeting.objects.create(
                requester = request.user,
                requested =requested,
                date = request.POST.get('date'),
                start_time = request.POST.get('start_time'),
                end_time = request.POST.get('end_time'),
                remarks = request.POST.get('remarks'),
            )
    messages.success(request,msg)
    return redirect(url)

@login_required
def reject_or_accept_a_meeting(request,meeting_id,tab):
    url = request.META.get('HTTP_REFERER')
    requested = request.user
    status= ''
    msg = ''
    obj = get_object_or_404(models.Meeting, id=meeting_id)
    if not obj.requested == None:
        requested = obj.requested
    accepted =request.POST.get('accepted')
    rejected = request.POST.get('rejected')
    if accepted:
        status = True
        msg = accepted
    if rejected:
        status = False
        msg = rejected
    obj.was_meeting_accepted = status
    obj.requested = requested
    obj.save()
    messages.success(request,'Meeting was successfully {}'.format(msg))
    return redirect(url)

@login_required
def reschedule_a_meeting(request, meeting_id,tab):
    url = request.META.get('HTTP_REFERER')
    meeting_obj = get_object_or_404(models.Meeting,id=meeting_id)
    date  = request.POST.get('date')
    time = request.POST.get('time')
    meeting_obj.date = date
    meeting_obj.time = time
    meeting_obj.requester = request.user
    meeting_obj.requested = get_object_or_404(m.User, id = meeting_obj.requester)
    meeting_obj.save()
    #sent a meeting resheduled
    messages.success(request,'Meeting successfully rescheduled to {} at {}'.format(date,time))
    return redirect(url)

@login_required
def meetings(request):
    template_name = 'meetings.html'
    user=  request.user
    date_today = dt.date.today()
    meetings_qs = models.Meeting.objects.filter(requested = user)
    print(meetings_qs)
    requested_meetings_incoming = meetings_qs
    requested_meetings_outgoing = models.Meeting.objects.filter(requester = user)
    upcoming_meetings = meetings_qs.filter(was_meeting_accepted = True)
    past_meetings = meetings_qs.filter(date__lt = date_today).filter(was_meeting_accepted = True).filter(was_meeting_attended = True)
    brodcast_meeting = models.Meeting.objects.filter(requested = None).filter(was_meeting_accepted = None)
    form  = forms.MeetingForm()
    context = {
        "upcoming_meetings": upcoming_meetings,
        "incoming_meetings" : requested_meetings_incoming,
        "outgoing_meetings": requested_meetings_outgoing,
        "past_meetings":past_meetings,
        "brodcast_meetings":brodcast_meeting,
        "form":form
    }
    return render(request,template_name, context)


