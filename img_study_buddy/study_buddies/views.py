from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User

# Create your views here.
@login_required
def view_all_study_buddies(request):
    template_name = 'view_all_study_buddies.html'
    candidates_qs = get_list_or_404(User,is_candidate = True,is_registration_complete=True)
    context = {
        'obj':candidates_qs
    }
    return render(request,template_name,context)
