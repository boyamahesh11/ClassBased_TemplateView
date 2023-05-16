from django import forms

from app.models import *

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        