from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from easy_meal_challenge.accounts.models import Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('avatar_url', 'bio')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['username'].initial = user.username
        self.fields['email'].initial = user.email

        self.user = user

    def save(self, commit=True):
        profile = super().save(commit=False)

        self.user.username = self.cleaned_data['username']
        self.user.email = self.cleaned_data['email']

        if commit:
            self.user.save()
            profile.save()

        return profile