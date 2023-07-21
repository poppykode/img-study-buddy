import uuid
from django.forms import formset_factory
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from . import forms


app_name = 'accounts'

coach_reg_forms = [
    forms.GeneralAdditionalInfoForm,
    forms.EducationForm,
    forms.WorkExperienceForm, 
    forms.CoachAdditionalInfoForm,
    forms.MotivationForm
]

candidate_reg_forms = [
    forms.GeneralAdditionalInfoForm,
    forms.CandidateAdditionalInfoForm
]


urlpatterns = [
  
    path('',views.login, name='login'),
    path('coach-dashboard',views.coach_dashboard,name='coach_dashboard'),
    path('admin-dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('candidate-dashboard',views.candidate_dashboard,name='candidate_dashboard'),
    path('q/save-coach-data',views.save_coach_data, name='save_coach_data'),
    path('p/save-candidate-data',views.save_candidate_data, name='save_candidate_data'),
    path('register',views.register, name='register'),
    path('redirect',views.redirect_logged, name='redirect_logged'),
    path('registration-wizard/<int:form_number>',views.handle_sessions_forward, name='handle_sessions_forward'),
    path('registration-view-wizard/<int:form_number>',views.handle_form_displays, name='handle_form_displays'),
    path('{{uuid.uuid4().hex}}',login_required(views.RegCoachWizard.as_view(coach_reg_forms)), name='reg_wiz_coach'),
    path('{{uuid.uuid4().hex}}',login_required(views.RegCandidateWizard.as_view(candidate_reg_forms)), name='reg_wiz_candidate'),
    path('coach-application-preview',views.coach_application_preview, name='coach_application_preview'),
    path('profile',views.profile, name='profile'),
    path('public-profile/<uuid:user_id>',views.public_profile,name='public_profile'),
    path('users',views.users, name='users')

]
