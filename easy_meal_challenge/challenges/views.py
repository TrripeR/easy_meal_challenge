from django.shortcuts import render
from django.views.generic import  DetailView

from easy_meal_challenge.challenges.models import Challenge
from easy_meal_challenge.recipes.models import Recipe


# Create your views here.
class ActiveChallengeView(DetailView):
    model = Challenge
    template_name = 'challenges/active_challenge.html'
    context_object_name = 'challenge'

    def get_object(self):
        return Challenge.objects.filter(is_active=True).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenge = self.get_object()

        context['recipes'] = Recipe.objects.filter(challenge=challenge) if challenge else []

        if self.request.user.is_authenticated and challenge:
            profile = self.request.user.profile
            context['user_has_submitted'] = Recipe.objects.filter(challenge=challenge, author=profile).exists()
        else:
            context['user_has_submitted'] = False

        return context