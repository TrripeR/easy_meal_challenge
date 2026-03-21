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
        fields = ('username', 'email', 'first_name', 'last_name', 'cooking_exp', 'avatar')


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['avatar'].widget.attrs['class'] = 'form-control-file'

        self.fields['username'].initial = user.username
        self.fields['email'].initial = user.email

        self.user = user

        if self.instance:
            self.fields['first_name'].initial = self.instance.first_name
            self.fields['last_name'].initial = self.instance.last_name
            self.fields['cooking_exp'].initial = self.instance.cooking_exp
            self.fields['avatar'].initial = self.instance.avatar

    def save(self, commit=True):
        profile = super().save(commit=False)

        self.user.username = self.cleaned_data['username']
        self.user.email = self.cleaned_data['email']

        if commit:
            self.user.save()
            profile.save()

        return profile