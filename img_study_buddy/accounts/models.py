import pytz
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from review_ratings.models import ReviewRating
from meetings.models import Meeting
from django.db.models import Avg, Count
from tinymce.models import HTMLField
from django.db.models import Q

# Create your models here.
class User (AbstractUser):
    PENDING ='pending'
    STATUS = (('accepted','Accepted'),('rejected','Rejected'),(PENDING,'Pending'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_candidate = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_registration_complete = models.BooleanField(default=False)
    is_coach_accepted = models.BooleanField(default=True)
    account_status = models.CharField(max_length=10,choices=STATUS,default=PENDING)

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize() + ' | ' + str(self.email)

    class Meta:
        ordering = ["-date_joined", ]

    def averageReview(self):
        reviews = ReviewRating.objects.filter(user_rated=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(user_rated=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    def meetings_attended(self):
        count = 0
        meetings = Meeting.objects.filter(requested = self).filter(was_meeting_accepted=True).filter(was_meeting_attended=True).aggregate(count=Count('id'))
        if meetings['count'] is not None:
            count = int(meetings['count'])
        return count

    def reliability(self):
        attended_meetings_count = 0
        total_meetings_count = 0
        percentage_attandence = 0
        attended_meetings = Meeting.objects.filter(requested = self).filter(was_meeting_accepted=True).filter(was_meeting_attended=True).aggregate(count=Count('id'))
        total_meetings = Meeting.objects.filter(requested = self).filter(was_meeting_accepted=True).exclude(was_meeting_cancelled = True).aggregate(count=Count('id'))
        if attended_meetings['count'] is not None:
            attended_meetings_count = int(attended_meetings['count'])
        if total_meetings['count'] is not None:
            total_meetings_count = int(total_meetings['count'])
        if attended_meetings_count > 0 and total_meetings_count > 0:
            percentage_attandence = (attended_meetings_count/total_meetings_count) * 100
        return percentage_attandence

        
class GeneralAdditionalInfo(models.Model):
    GENDER=(('','select a gender'),
            ('male','Male'),
            ('female','Female'),
            ('diversity','Diversity')
            )
    user=models.OneToOneField(User,related_name='user_general_additional_info', on_delete=CASCADE)
    gender = models.CharField(max_length=10,choices=GENDER)
    time_zone = models.CharField(max_length=255,choices=[(x,x) for x in pytz.all_timezones_set])
    phone_number = models.CharField(max_length=255, null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class CandidateAdditionalInfo(models.Model):
    user=models.OneToOneField(User,related_name='user_candidate_additional_info', on_delete=CASCADE)
    exam_date = models.DateField()
    availability = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class WorkExperience(models.Model):
    user=models.ForeignKey(User,related_name='user_work_experience', on_delete=CASCADE)
    name_of_hospital = models.CharField(max_length=255)
    country_of_hospital = models.CharField(max_length=255)
    position_at_the_hospital = models.CharField(max_length=255)
    period_from =models.DateField()
    period_to = models.DateField() 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class Education(models.Model):
    user=models.ForeignKey(User,related_name='user_education', on_delete=CASCADE)
    name_of_instutution = models.CharField(max_length=255)
    period_from =models.DateField()
    period_to = models.DateField() 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class Motivation(models.Model):
    user=models.OneToOneField(User,related_name='user_motivation', on_delete=CASCADE)
    description = HTMLField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]

class CoachAdditionalInfo(models.Model):
    user=models.OneToOneField(User,related_name='user_coach_additional_info', on_delete=CASCADE)
    cv = models.FileField(upload_to='files')
    nhs_experience = models.CharField(max_length=255)
    rate = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]




