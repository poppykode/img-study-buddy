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
    path('users',views.users, name='users'),
    path('admin-profile/<uuid:coach_id>',views.admin_profile, name='admin_profile'),
    path('accept-or-reject_application/<uuid:coach_id>/<str:status>',views.accept_or_reject_application, name='accept_or_reject_application'),
    path('activate-or-deactivate_account/<uuid:user_id>',views.activate_or_deactivate_account, name='activate_or_deactivate_account'),
    path('add-admin',views.add_admin, name='add_admin'),
    path('change-password',views.change_password, name='change_password'),
    path('upload-profile-picture',views.upload_profile_picture, name='upload_profile_picture'),
    path('update-general-additional-info',views.update_general_additional_info, name='update_general_additional_info'),
    path('update-exam-date-and-availability',views.update_exam_date_and_availability, name='update_exam_date_and_availability'),
]

