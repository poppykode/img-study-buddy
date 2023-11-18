from django import forms
from . import models
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import PasswordChangeForm
from datetime import date, datetime

class ProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField(
        help_text="Allowed JPG or PNG",
        widget= forms.FileInput(attrs={'accept': 'image/png, image/jpeg, image/jpg'}))

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''


class GeneralAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = models.GeneralAdditionalInfo
        fields = ('gender','time_zone','phone_number','profile_picture')

class CandidateAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = models.CandidateAdditionalInfo
        widgets = {
            'exam_date': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date'}),
        }
        labels = {
            'availability':'Availability (hrs per day)'
        }

        fields = ('exam_date','availability',)

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = models.WorkExperience
        widgets = {
            'period_from': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date'}),
            'period_to': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date'}),
        }

        fields = ('name_of_hospital','country_of_hospital','position_at_the_hospital','period_from','period_to')

class EducationForm(forms.ModelForm):
    class Meta:
        model = models.Education
        widgets = {
            'period_from': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date'}),
            'period_to': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date'}),
        }

        fields = ('name_of_instutution','period_from','period_to')

class MotivationForm(forms.ModelForm):
    class Meta:
        model = models.Motivation
        widgets = {
          'description': TinyMCE(attrs={'rows':4, 'cols':15}),
        }
        fields = ('description',)

class CoachAdditionalInfoForm(forms.ModelForm):
    class Meta:
        labels={
            'nhs_experience':'NHS Experience(months)',
            'cv':'Upload your CV (PDF Format)',
            'rate':'Rate/hour'
            }
        widgets = {
            'cv': forms.FileInput(attrs={'accept': 'application/pdf'})
            }
        model = models.CoachAdditionalInfo
        fields = ('rate','cv','nhs_experience')

class ExamDateAndAvailabiltyForm(forms.ModelForm):
    class Meta:
        model = models.CandidateAdditionalInfo
        labels = {
            'availability':'Availability (hrs per day)'
        }
        widgets = {
            'exam_date': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date', 'min':date.today()})
        }
        fields = ('exam_date','availability',)

        def clean(self):
            cleaned_data = super().clean()
            exam_date = self.cleaned_data['exam_date']
            availability = self.cleaned_data['availability']
            if exam_date < date.today():
                raise forms.ValidationError("Date cannot be in the past.")
            if availability < 0:
                raise forms.ValidationError("Availability cannot be less than 0 hrs per day.")
            return cleaned_data


