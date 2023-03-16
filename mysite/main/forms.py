from django import forms
from . import models


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['user_name', 'user_email', 'user_review']