from django import forms
from . import models

class MeetingForm(forms.ModelForm):
    class Meta:
        model = models.Meeting
        widgets = {
            'remarks': forms.Textarea(attrs={'rows':4, 'cols':15}),
            'date': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date', 'id':'html5-time-input'}),
            'start_time': forms.widgets.DateInput(attrs={'class': 'datepicker', 'type': 'time', 'id':'html5-time-input'}),
            'end_time': forms.widgets.DateInput(attrs={'class': 'datepicker', 'type': 'time', 'id':'html5-time-input'}),
        }
        labels = {
            'remarks':'Remarks (Optional)'
        }

        fields = ('date','start_time','end_time','remarks')



