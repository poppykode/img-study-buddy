from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.core.paginator import Paginator

# Create your views here.
@login_required
def view_all_study_buddies(request):
    template_name = 'view_all_study_buddies.html'
    # candidates_qs = get_list_or_404(User,is_candidate = True,is_registration_complete=True)
    candidates_qs = User.objects.filter(is_candidate = True,is_registration_complete=True).exclude(id=request.user.id)
    paginator = Paginator(candidates_qs, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'obj':page_obj,
        'candidates':len(candidates_qs)
    }
    return render(request,template_name,context)
