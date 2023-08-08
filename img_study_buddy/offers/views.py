from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models

# Create your views here.

@login_required
def offer_details(request,user_id):
    template_name = 'offer_details.html'
    obj = get_object_or_404(models.Offer,user=user_id)
    context ={'obj':obj}
    return render(request,template_name,context)
