from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Meeting(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE,related_name='meeting_requester')
    requested = models.ForeignKey(User, on_delete=models.CASCADE,related_name='meeting_requested')
    station = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    Remarks = models.TextField()
    requested_has_accepted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.requester.first_name +' '+ self.requested.first_name
    
    class Meta:
        ordering = ["timestamp",]

