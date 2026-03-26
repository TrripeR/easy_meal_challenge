from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

from easy_meal_challenge.challenges.forms import ChallengeCreateForm, ChallengeUpdateForm
from easy_meal_challenge.challenges.models import Challenge
from easy_meal_challenge.recipes.models import Recipe


# Create your views here.
class ActiveChallengeView(DetailView):
    model = Challenge
    template_name = 'challenges/active_challenge.html'
    context_object_name = 'challenge'

    def get_object(self):
        return Challenge.get_active()

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


from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class ChallengeUpdateView(UserPassesTestMixin, UpdateView):
    model = Challenge
    form_class = ChallengeUpdateForm
    template_name = 'challenges/update_challenge.html'
    success_url = reverse_lazy('active-challenge')

    def test_func(self):
        return self.request.user.is_staff

from django.views.generic import CreateView

class ChallengeCreateView(UserPassesTestMixin, CreateView):
    model = Challenge
    form_class = ChallengeCreateForm
    template_name = 'challenges/create_challenge.html'
    success_url = reverse_lazy('active-challenge')

    def test_func(self):
        return self.request.user.is_staff

class ChallengeListView(ListView):
    model = Challenge
    template_name = 'challenges/challenge_list.html'
    context_object_name = 'challenges'
    ordering = ['-start_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        challenges_with_recipes = []

        for challenge in context['challenges']:
            top_recipes = Recipe.objects.filter(
                challenge=challenge
            ).annotate(
                like_count=Count('likes')
            ).order_by('-like_count')[:3]

            challenges_with_recipes.append({
                'challenge': challenge,
                'top_recipes': top_recipes
            })

        context['challenge_data'] = challenges_with_recipes
        return context