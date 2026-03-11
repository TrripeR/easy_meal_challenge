from django.contrib.auth.views import LogoutView
from django.urls import path

from easy_meal_challenge.accounts.views import UserLoginView, UsersRegisterView, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UsersRegisterView.as_view(), name='register'),
    path('proffile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit', ProfileUpdateView.as_view(), name='profile-edit'),
]