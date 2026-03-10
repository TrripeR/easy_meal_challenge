from django.contrib import admin


from easy_meal_challenge.recipes.models import Recipe, Like


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'challenge', 'created_at')
    list_filter = ('challenge',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')
