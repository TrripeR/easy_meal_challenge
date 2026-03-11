from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from easy_meal_challenge.accounts.models import Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar_url', 'bio',)