from django.urls import path

from easy_meal_challenge.challenges.views import ActiveChallengeView

urlpatterns = [
    path('active/', ActiveChallengeView.as_view(), name='active-challenge'),
]