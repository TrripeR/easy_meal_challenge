from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from easy_meal_challenge.accounts.models import Profile
from easy_meal_challenge.challenges.models import Challenge
from easy_meal_challenge.recipes.forms import RecipeCreateForm, RecipeUpdateForm
from easy_meal_challenge.recipes.models import Recipe, Like


# Create your views here.

class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/recipe_create.html'
    success_url = reverse_lazy('active-challenge')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        challenge = Challenge.objects.filter(is_active=True).first()
        kwargs["initial"]["challenge"] = challenge

        return kwargs

    def form_valid(self, form):
        challenge  = Challenge.objects.filter(is_active=True).first()

        form.instance.author = self.request.user.profile
        form.instance.challenge = challenge

        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_details.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['recipe'] = recipe

        if self.request.user.is_authenticated:
            context['user_liked'] = Like.objects.filter(
                recipe=recipe,
                user=self.request.user
            ).exists()

        return context


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = 'recipes/recipe_update.html'

    def get_success_url(self):
        return reverse_lazy('recipe-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_delete.html'
    success_url = reverse_lazy('active-challenge')

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user


class WinnerListView(ListView):
    model = Recipe
    template_name = 'recipes/winners.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(is_winner=True)


def toggle_like(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Get or create the profile for logged-in user
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile.objects.create(user=request.user)

    # Check if this profile already liked the recipe
    like_instance = Like.objects.filter(recipe=recipe, user=profile).first()

    if like_instance:
        # Already liked → remove it
        like_instance.delete()
    else:
        # Not liked yet → create a new Like
        Like.objects.create(recipe=recipe, user=profile)

    # Redirect back to the page you want (e.g., active challenge)
    return redirect('active-challenge')