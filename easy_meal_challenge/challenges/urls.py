from django.urls import path

from easy_meal_challenge.challenges.views import ActiveChallengeView, ChallengeCreateView, ChallengeUpdateView

urlpatterns = [
    path('active/', ActiveChallengeView.as_view(), name='active-challenge'),
    path('create/', ChallengeCreateView.as_view(), name='challenge-create'),
    path('update/<int:pk>/', ChallengeUpdateView.as_view(), name='challenge-update'),
]