from django.db import models
from django.conf import settings
from review_ratings import models as m
from django.db.models import Avg, Count


User = settings.AUTH_USER_MODEL
# Create your models here.
class Offer(models.Model):
    user=models.ForeignKey(User,related_name='user_offers', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='offers')
    file = models.FileField(upload_to='files')
    summary = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ["-timestamp", ]


    def averageReview(self):
        reviews = m.OfferReviewRating.objects.filter(offer=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = m.OfferReviewRating.objects.filter(offer=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
