import uuid
import datetime as dt
from django.db import models
from django.conf import settings
from tinymce.models import HTMLField

User = settings.AUTH_USER_MODEL

# Create your models here.

class Meeting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requester = models.ForeignKey(User, on_delete=models.CASCADE,related_name='meeting_requester')
    requested = models.ForeignKey(User, on_delete=models.CASCADE,related_name='meeting_requested',null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    remarks = HTMLField(blank=True,null=True)
    was_meeting_accepted = models.BooleanField(null=True)
    was_meeting_attended = models.BooleanField(null=True)
    was_meeting_cancelled = models.BooleanField(null=True)
    was_meeting_rejected = models.BooleanField(null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.requester.first_name
    
    class Meta:
        ordering = ["timestamp",]

    @property
    def is_date_in_the_past(self):
        if self.date > dt.date.today():
            return False
        return True

