from django import forms
from . import models
from tinymce.widgets import TinyMCE

class OfferForm(forms.ModelForm):
    class Meta:
        model = models.Offer
        widgets = {
          'summary': TinyMCE(attrs={'rows':4}),
          'description': TinyMCE(attrs={'rows':4}),
        }
        fields = ('title','image','file','summary','description','price')


