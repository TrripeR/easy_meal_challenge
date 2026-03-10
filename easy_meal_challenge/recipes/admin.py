from django.contrib import admin


from easy_meal_challenge.recipes.models import Recipe, Like


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'challenge', 'ingredients_count', 'likes_count', 'is_winner', 'created_at')
    list_filter = ('challenge', 'is_winner')
    search_fields = ('title', 'author__user__username')
    ordering = ('-created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')
