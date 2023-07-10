from django.urls import path
from . import views


app_name = 'review_ratings'
urlpatterns = [
    path('create-review/<int:user_id>',views.create_review, name='create_review')
]
