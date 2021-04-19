from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        widgets = {

        }

class stud_details(forms.ModelForm):
    class Meta:
        model=stud
        fields=[
            'name',
            'id',
            'age',
            'phone',
            'mark',
            'image',

        ]
