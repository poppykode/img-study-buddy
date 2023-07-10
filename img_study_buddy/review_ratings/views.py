from django.shortcuts import render, get_object_or_404,redirect
from . import models
from accounts.models import  User
from django.contrib import messages

# Create your views here.
def create_review(request,user_id):
    url = request.META.get('HTTP_REFERER')
    user_ = request.user
    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            rating = request.POST.get('rating')
        else:
            rating = 0.0
        review = request.POST.get('review')
        user_rated = get_object_or_404(User,id=user_id)
        user_has_commented = models.ReviewRating.objects.filter(user_rating=user_,user_rated=user_rated).exists()
        if not user_has_commented:
            models.ReviewRating.objects.create(
                user_rating = user_,
                review = review,
                rating = rating,
                user_rated = user_rated,
                ip=request.META.get('REMOTE_ADDR')
            )
            messages.success(request, 'Review successfully updated.')
        else:
            messages.warning(request, 'You can only submit one review.')
    return redirect(url)
