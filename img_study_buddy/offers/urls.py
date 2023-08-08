from django.urls import path
from . import views


app_name = 'offers'
urlpatterns = [
    path('offer-details/<uuid:user_id>',views.offer_details, name='offer_details')
]
