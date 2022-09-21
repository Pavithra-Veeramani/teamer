from .models import Member
from django import forms
from django.forms import ModelForm, CharField, TextInput

class EditMemberForm(forms.ModelForm):
    phone_number = CharField(widget=TextInput(attrs={'type': 'tel'}))
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'phone_number')
