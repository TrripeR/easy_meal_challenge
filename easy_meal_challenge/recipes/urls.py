from django.urls import path

from easy_meal_challenge.recipes.views import RecipeCreateView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView, \
    WinnerListView, toggle_like, award_winner

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-details'),
    path('<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe-edit'),
    path('<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('winners/', WinnerListView.as_view(), name='winners'),
    path('<int:pk>/like/', toggle_like, name='toggle-like'),
    path('recipe/<int:pk>/award/', award_winner, name='award-winner'),
]