from django import forms
from easy_meal_challenge.challenges.models import Challenge


class ChallengeCreateForm(forms.ModelForm):

    class Meta:
        model = Challenge
        fields = ('title', 'description', 'required_ingredients', 'max_ingredients', 'theme', 'start_date', 'end_date', 'is_active' )

        widgets = {
            'start_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                }
            ),
            'end_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and end and end <= start:
            raise forms.ValidationError("End date must be after start date.")

        return cleaned_data


class ChallengeUpdateForm(forms.ModelForm):

    class Meta:
        model = Challenge
        fields = ('title', 'description', 'required_ingredients', 'max_ingredients', 'theme', 'start_date', 'end_date', 'is_active')

        widgets = {
            'start_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                }
            ),
            'end_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                }
            ),
        }
