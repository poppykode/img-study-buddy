from django.urls import path
from . import views


app_name = 'meetings'
urlpatterns = [
    path('create-a-meeting',views.create_a_meeting,name='create_a_meeting'),
    path('create-a-meeting/<uuid:requested_id>',views.create_a_meeting,name='create_a_meeting'),
    path('meetings-board',views.meetings,name='meetings'),
    path('reschedule-a-meeting/<uuid:meeting_id>/<str:tab>',views.reschedule_a_meeting,name='reschedule_a_meeting'),
    path('reject-or-accept-a-meeting/<uuid:meeting_id>/<str:tab>',views.reject_or_accept_a_meeting,name='reject_or_accept_a_meeting'),

]
