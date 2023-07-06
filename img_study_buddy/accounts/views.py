import os
import json
import base64
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.serializers.json import DjangoJSONEncoder

from img_study_buddy.utils import (
    has_session,
    delete_a_file,
    deserialise_,
    serialise_,
    complete_registration,
    dash_board_redirect
    
) 
from . import forms
from accounts.models import User
from . import models



# FORMS = [("general", forms.GeneralAdditionalInfoForm),
#          ("candidate", forms.CandidateAdditionalInfoForm),
#          ("work", forms.WorkExperienceForm),
#          ("education", forms.EducationForm),
#          ("motivation", forms.MotivationForm),
#          ("coach", forms.CoachAdditionalInfoForm)]

COACH_TEMPLATES = {
    "0": "wizard/general_additional_Info_form.html",
    "1": "wizard/education_form.html",
    "2": "wizard/work_experience_form.html",
    "3": "wizard/coach_additional_Info_form.html",
    "4": "wizard/motivation_form.html",
    
}

CANDIDATE_TEMPLATES = {
    "0": "wizard/general_additional_Info_form.html",
    "1": "wizard/candidate_additional_Info_form.html",
    }

# Create your views here.
class RegCoachWizard(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT))
    def get_template_names(self):
        return [COACH_TEMPLATES[self.steps.current]]

    def done(self,form_list, **kwargs):  #Required
        form_data = [form.cleaned_data for form in form_list]
        education_info_form = form_list[1]
        name_of_instutution = education_info_form.cleaned_data['name_of_instutution'][0]
 
        return redirect('accounts:coach_dashboard')
    

class RegCandidateWizard(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT))
    def get_template_names(self):
        return [CANDIDATE_TEMPLATES[self.steps.current]]

    def done(self,form_list, **kwargs):
        general_info_form = form_list[0]
        general_info = general_info_form.save(commit=False)
        general_info.user = self.request.user
        general_info.save()
        candidate_Info_form = form_list[1]
        candidate_Info = candidate_Info_form.save(commit=False)
        candidate_Info.user = self.request.user
        candidate_Info.save()
        user = get_object_or_404(User,id=self.request.user.id)
        user.is_registration_complete = True
        user.save()
        return redirect('accounts:candidate_dashboard')

@login_required
def handle_sessions_forward(request,form_number):
    user =  request.user
    session_key = settings.GENERAL_INFO
    filename = ''
    profile_picture_ = ''
    if form_number == 1:

        profile_picture=request.FILES.get('profile_picture')
        print('_____')
        print(profile_picture)
        print(type(profile_picture))
        print('_____')
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,settings.PROFILE_PICTURES))
        if not profile_picture == None:            
            filename = fs.save(profile_picture.name, profile_picture.file)
            profile_picture_=settings.PROFILE_PICTURES +'/'+filename
        else:
            print('if none this runs')
            filename = request.POST.get('filename')
            profile_picture_ = request.POST.get('profile_picture_1')
        # if not request.session.get(session_key,None) == None :
        #     delete_a_file(request,session_key,fs,form_number)
        general_info_ =  {
            'gender':request.POST.get('gender'),
            'time_zone':request.POST.get('time_zone'),
            'phone_number':request.POST.get('phone_number'),
            'profile_picture_name':filename,
            'profile_picture':profile_picture_
        }
        #create a session of general info
        request.session[session_key]=serialise_(general_info_)
        #next button 
        if user.is_candidate:
            return redirect('accounts:handle_form_displays',(form_number+1))
        return redirect('accounts:handle_form_displays',(form_number+2))
    elif form_number == 2:
        candidate_info_ =  {
            'exam_date':request.POST.get('exam_date'),
            'availability':request.POST.get('availability'),
        }   
        #create session for candidate info
        request.session[settings.CANDIDATE_INFO]=serialise_(candidate_info_)
        #next button
        return redirect('accounts:save_candidate_data')  
    elif form_number == 3:
        education_info_ = [
        ]
        name_of_instutution=request.POST.getlist('name_of_instutution')
        c = len(name_of_instutution)
        for item in range(c):
            education_info_.append(
                { 
                    'name_of_instutution':name_of_instutution[item],
                    'period_from':request.POST.getlist('period_from')[item],
                    'period_to':request.POST.getlist('period_to')[item],
                }
            )
        request.session[settings.EDUCATION_INFO]=serialise_(education_info_)
        #next button
        return redirect('accounts:handle_form_displays',(form_number+1))
    elif form_number == 4:
        work_experienceForm_info_ = [
        ]
        name_of_hospital=request.POST.getlist('name_of_hospital')
        c = len(name_of_hospital)
        for item in range(c):
            work_experienceForm_info_.append(
                {
                    'name_of_hospital':name_of_hospital[item],
                    'country_of_hospital':request.POST.getlist('country_of_hospital')[item],
                    'position_at_the_hospital':request.POST.getlist('position_at_the_hospital')[item],
                    'period_from':request.POST.getlist('period_from')[item],
                    'period_to':request.POST.getlist('period_to')[item],
                }
            )
        request.session[settings.WORK_EXPERIENCE_INFO]=serialise_(work_experienceForm_info_)
        #next button
        return redirect('accounts:handle_form_displays',(form_number+1))
    elif form_number == 5:
        motivation_info_ = {
            'description':request.POST.get('description'),
        }

        request.session[settings.MOTIVATION_INFO]=serialise_(motivation_info_)
        #next button
        return redirect('accounts:handle_form_displays',(form_number+1))
    else:
        cv=request.FILES.get('cv') 
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,settings.FILES))
        filename = fs.save(cv.name, cv.file)
        cv_url=settings.FILES +'/'+filename
        coach_info_ = {
            'cv':cv_url,
            'nhs_experience':request.POST.get('nhs_experience'),
        }
    
        request.session[settings.COACH_INFO]=serialise_(coach_info_)
        #next button
        return redirect('accounts:save_coach_data')

@login_required
def handle_form_displays(request,form_number):
    if form_number == 1:
        template_name = 'wizard/general_additional_Info_form.html'
        form =''
        img=''
        name =''
        key = settings.GENERAL_INFO
        if has_session(request,key):
            general_info_=deserialise_(request.session[key])
            print(general_info_)
            form = forms.GeneralAdditionalInfoForm(initial=general_info_)
            img = general_info_['profile_picture']
            name = general_info_['profile_picture_name']
        else:
            form = forms.GeneralAdditionalInfoForm()
        return render(request,template_name,{'form':form,'form_number':form_number,'img':img,'name':name})
    elif form_number == 2:
            template_name = 'wizard/candidate_additional_Info_form.html'
            form =''
            key = settings.CANDIDATE_INFO
            if has_session(request,key):
                candidate_info_= deserialise_(request.session[key])
                form = forms.CandidateAdditionalInfoForm(initial=candidate_info_)
            else:
                form = forms.CandidateAdditionalInfoForm()      
            return render(request,template_name,{'form':form,'form_number':form_number,'image_':''})
    
    elif form_number == 3:
            template_name = 'wizard/education_form.html'
            form =''
            back_step = False
            obj=[]
            key = settings.EDUCATION_INFO
            if has_session(request,key):
                education_info_= deserialise_(request.session[key])
                for item in education_info_:
                    obj.append({
                        'name_of_instutution':item['name_of_instutution'],
                        'period_from':item['period_from'],
                        'period_to':item['period_to'],
                    })
                back_step = True
            form = forms.EducationForm()

            return render(request,template_name,{'form':form,'obj':obj,'form_number':form_number,'back_step':back_step})
    elif form_number == 4:
            template_name = 'wizard/work_experience_form.html'
            form =''
            back_step = False
            obj=[]
            key = settings.WORK_EXPERIENCE_INFO
            if has_session(request,key):
                work_experienceForm_info_= deserialise_(request.session[key])
                for item in work_experienceForm_info_:
                    obj.append({
                        'name_of_hospital':item['name_of_hospital'],
                        'country_of_hospital':item['country_of_hospital'],
                        'position_at_the_hospital':item['position_at_the_hospital'],
                        'period_from':item['period_from'],
                        'period_to':item['period_to'],
                    })
                back_step = True       
            form = forms.WorkExperienceForm()
            return render(request,template_name,{'form':form,'obj':obj,'form_number':form_number,'back_step':back_step})   

    elif form_number == 5:
        template_name = 'wizard/motivation_form.html'
        form =''
        key = settings.MOTIVATION_INFO
        if has_session(request,key):
            motivation_info_= deserialise_(request.session[key])
            form = forms.MotivationForm(initial=motivation_info_)
        else:
            form = forms.MotivationForm()
        return render(request,template_name,{'form':form,'form_number':form_number})   
    else:
        template_name = 'wizard/coach_additional_Info_form.html'
        form =''
        key = settings.COACH_INFO
        if has_session(request,key):
            coach_info_= deserialise_(request.session[key])
            form = forms.CoachAdditionalInfoForm(initial=coach_info_)
        else:
            form = forms.CoachAdditionalInfoForm()
        return render(request,template_name,{'form':form,'form_number':form_number})

def create_general_info(general_info,user):
    models.GeneralAdditionalInfo.objects.create(
        user = user,
        gender =general_info['gender'],
        time_zone = general_info['time_zone'],
        phone_number = general_info['phone_number'],
        profile_picture = general_info['profile_picture'],
    )
 
@login_required
def save_coach_data(request):
    user = request.user
    general_info = deserialise_(request.session[settings.GENERAL_INFO])
    education_info = deserialise_(request.session[settings.EDUCATION_INFO])
    work_experience_info = deserialise_(request.session[settings.WORK_EXPERIENCE_INFO])
    motivation_info = deserialise_(request.session[settings.MOTIVATION_INFO])
    coach_info = deserialise_(request.session[settings.COACH_INFO])
    create_general_info(general_info,user)

    for item in education_info:
        models.Education.objects.create(
            user=user,
            name_of_instutution = item['name_of_instutution'],
            period_from = item['period_from'],
            period_to = item['period_to'],
        )

    for item in work_experience_info:
        models.WorkExperience.objects.create(
            user=user,
            name_of_hospital = item['name_of_hospital'],
            country_of_hospital = item['country_of_hospital'],
            position_at_the_hospital = item['position_at_the_hospital'],
            period_from = item['period_from'],
            period_to = item['period_to'],
        )

    models.Motivation.objects.create(
        user = user,
        description =motivation_info['description'],
    )
    models.CoachAdditionalInfo.objects.create(
        user = user,
        cv =coach_info['cv'],
        nhs_experience =coach_info['nhs_experience'] ,
    )
    complete_registration(request,settings.KEYS)
    return redirect('accounts:redirect_logged')

@login_required
def save_candidate_data(request):
    user = request.user
    general_info = deserialise_(request.session[settings.GENERAL_INFO])
    canditate_info = deserialise_(request.session[settings.CANDIDATE_INFO])
    create_general_info(general_info,user)
    models.CandidateAdditionalInfo.objects.create(
        user=user,
        exam_date = canditate_info['exam_date'],
        availability = canditate_info['availability']
    )
    complete_registration(request,settings.KEYS)

    print('candidate data saved')
    return redirect('accounts:redirect_logged')

@login_required
def redirect_logged(request):
    user = request.user
    print('entry')
    if not user.is_admin:
        if not user.is_registration_complete:
            print('registration incomplete')
            return redirect('accounts:handle_form_displays',1)
        elif user.is_registration_complete and not user.is_coach_accepted:
            print('registration complete but not accepted')
            return redirect('accounts:coach_application_preview')
        else:
            print('registration complete and accepted')
            return dash_board_redirect(user)
    print('for admin')
    return redirect('accounts:admin_dashboard')


@login_required  
def coach_application_preview(request):
    template_name = 'coach_application_preview.html'

    return render(request, template_name, {'full_name':""})

@login_required  
def candidate_dashboard(request):
    template_name = 'dashboards/candidate_dashboard.html'
    return render(request, template_name)

@login_required  
def coach_dashboard(request):
    template_name = 'dashboards/coach_dashboard.html'
    return render(request, template_name)

@login_required  
def admin_dashboard(request):
    template_name = 'dashboards/admin_dashboard.html'
    return render(request, template_name)

def login(request):
    template_name = 'registration/login.html'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if not user.is_active:
                messages.error(
                    request, 'Your account has been deactivate, please contact IMGSTUDYBUDDY.')
                return render(request, template_name)
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect(reverse('accounts:redirect_logged'))
        messages.error(request, 'Invalid username or password.')
    return render(request, template_name)

def register(request):
    template_name = 'registration/register.html'
    username =request.POST.get('email')
    password = request.POST.get('password','')
    role = request.POST.get('role')
    if request.method == 'POST':
        is_candidate = False
        is_coach = False
        is_coach_accepted = False
        if role == 'candidate':
            is_candidate = True
            is_coach_accepted = True
        else:
            is_coach = True
        new_user = User.objects.create(
            username=username,
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email=username,
            is_candidate = is_candidate,
            is_coach = is_coach,
            is_coach_accepted = is_coach_accepted
        )
        new_user.set_password(password)
        new_user.save()
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('accounts:redirect_logged')
        messages.error(request, 'Something went wrong.')
    return render(request, template_name)

@login_required
def profile(request):
    template_name =  'registration/profile.html'
    user_qs = get_object_or_404(models.User, pk=request.user.pk)
    return render(request,template_name, {'obj':user_qs})

