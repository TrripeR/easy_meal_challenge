from django.shortcuts import render
from django.views.generic import  DetailView

from easy_meal_challenge.challenges.models import Challenge


# Create your views here.
class ActiveChallengeView(DetailView):
    model = Challenge
    template_name = 'challenges/active_challenge.html'
    context_object_name = 'challenge'

    def get_object(self):
        return Challenge.objects.get(is_active=True)

