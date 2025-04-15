from django import forms
from .models import Message
from django.forms.widgets import DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CapsuleForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'heading', 'content', 'unlock_datetime', 'visibility',
            'file', 'image', 'video',
            'latitude', 'longitude',  # <-- Add these fields
        ]
        widgets = {
            'unlock_datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
            # Optionally, you can hide these fields if you use a map picker in your template
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, help_text='First name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
