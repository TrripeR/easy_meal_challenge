from django.contrib import admin

from easy_meal_challenge.accounts.models import Badge
from easy_meal_challenge.recipes.models import Recipe, Like


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'challenge', 'ingredients_count', 'likes_count', 'is_winner', 'created_at')
    list_filter = ('challenge', 'is_winner')
    search_fields = ('title', 'author__user__username')
    ordering = ('-created_at',)

    actions = ["mark_as_winner"]

    @admin.action(description="Mark selected recipe as challenge winner")
    def mark_as_winner(self, request, queryset):

        if queryset.count() != 1:
            self.message_user(request, "Please select exactly ONE recipe.")
            return

        recipe = queryset.first()
        challenge = recipe.challenge

        Recipe.objects.filter(
            challenge=challenge
        ).update(is_winner=False)

        recipe.is_winner = True
        recipe.save()

        challenge.is_active = False
        challenge.save()

        badge = Badge.objects.filter(name="Challenge Winner").first()

        if badge:
            badge.users.add(recipe.author)

        Recipe.objects.filter(
            challenge=challenge,
            is_winner=False
        ).delete()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')
