from django import forms
from . import models
from datetime import date,datetime

class MeetingForm(forms.ModelForm):
    class Meta:
        model = models.Meeting
        widgets = {
            'remarks': forms.Textarea(attrs={'rows':4, 'cols':15}),
            'date': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date', 'min':date.today()}),
            'start_time': forms.widgets.TimeInput(attrs={'class': 'datepicker', 'type': 'time'}),
            'end_time': forms.widgets.TimeInput(attrs={'class': 'datepicker', 'type': 'time'}),
        }
        labels = {
            'remarks':'Remarks (Optional)'
        }
        fields = ('date','start_time','end_time','remarks')

    def clean(self):
        cleaned_data = super().clean()
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        date_ = self.cleaned_data['date']
        current_time = datetime.now().time()
        if date_ < date.today():
            raise forms.ValidationError("Date cannot be in the past.")
        if date_ == date.today() and start_time < current_time:
            raise forms.ValidationError(f"The meeting start time should be after {current_time.strftime('%H:%M')}")    
        if start_time > end_time:
            raise forms.ValidationError("Start time cannot be greater than end time.")
        return cleaned_data




