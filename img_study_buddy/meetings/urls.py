from django.urls import path
from . import views


app_name = 'meetings'
urlpatterns = [
    path('create-a-meeting/<uuid:requested_id>',views.create_a_meeting,name='create_a_meeting')

]
