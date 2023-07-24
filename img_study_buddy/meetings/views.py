from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from accounts import models as m

# Create your views here.

@login_required
def create_a_meeting(request,requested_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        models.Meeting.objects.create(
            requester = request.user,
            requested = get_object_or_404(m.User,id=requested_id),
            date = request.POST.get('date'),
            time = request.POST.get('time'),
            remarks = request.POST.get('remarks'),
        )
    messages.success(request,'Meeting request sent')
    return redirect(url)

