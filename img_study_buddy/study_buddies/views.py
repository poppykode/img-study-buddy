from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_all_study_buddies(request):
    template_name = 'view_all_study_buddies.html'
    return render(request,template_name)
