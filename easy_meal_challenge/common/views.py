from django.shortcuts import render
from django.views.generic import TemplateView

from easy_meal_challenge.challenges.models import Challenge
from easy_meal_challenge.recipes.models import Recipe


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_challenge = Challenge.objects.filter(is_active=True).first()
        context['challenge'] = active_challenge

        if active_challenge:
            context['recipes'] = Recipe.objects.filter(challenge=active_challenge).order_by('-created_at')

        return context


class AboutPageView(TemplateView):
    template_name = 'common/about.html'