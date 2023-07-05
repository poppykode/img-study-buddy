import pytz
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.
class User (AbstractUser):
    is_candidate = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_registration_complete = models.BooleanField(default=False)
    is_coach_accepted = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize() + ' | ' + str(self.email)

    class Meta:
        ordering = ["-date_joined", ]
        
class GeneralAdditionalInfo(models.Model):
    GENDER=(('','select a gender'),
            ('male','Male'),
            ('female','Female'),
            ('diversity','Diversity')
            )
    user=models.OneToOneField(User,related_name='user_general_additional_info', on_delete=CASCADE)
    gender = models.CharField(max_length=50,choices=GENDER)
    time_zone = models.CharField(max_length=255,choices=[(x,x) for x in pytz.common_timezones])
    phone_number = models.CharField(max_length=255, null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True,blank=True)
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
    description = models.TextField()
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
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.first_name.capitalize() + ' ' + self.user.last_name.capitalize() + ' | ' + str(self.user.email)

    class Meta:
        ordering = ["-timestamp", ]




