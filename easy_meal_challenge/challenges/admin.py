from django.contrib import admin

from easy_meal_challenge.challenges.models import Challenge
from easy_meal_challenge.recipes.models import Recipe


# Register your models here.

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'required_ingredients', 'theme', 'start_date', 'end_date', 'is_active',)
    list_filter = ('is_active' ,'theme',)
    search_fields = ('title', 'required_ingredients')

