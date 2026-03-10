from django.db import models

from easy_meal_challenge.accounts.models import Profile
from easy_meal_challenge.challenges.models import Challenge


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=120)
    ingredients = models.TextField(help_text="Enter one ingredient per line")
    instructions = models.TextField()
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.title

    @property
    def ingredients_list(self):
        return [i.strip() for i in self.ingredients.split("\n") if i.strip()]

    @property
    def ingredients_count(self):
        return len(self.ingredients_list)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user')