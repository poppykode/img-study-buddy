from django.urls import path
from . import views


app_name = 'meetings'
urlpatterns = [
    path('create-a-meeting',views.create_a_meeting,name='create_a_meeting'),
    path('create-a-meeting/<uuid:requested_id>',views.create_a_meeting,name='create_a_meeting'),
    path('meetings-board',views.meetings,name='meetings'),
    path('reschedule-a-meeting/<uuid:meeting_id>',views.reschedule_a_meeting,name='reschedule_a_meeting'),
    path('was-attended/<uuid:meeting_id>',views.was_attended,name='was_attended'),
    path('reject-accept-or-cancel-a-meeting/<uuid:meeting_id>/<str:type>',views.reject_accept_or_cancel_a_meeting,name='reject_accept_or_cancel_a_meeting'),

]
