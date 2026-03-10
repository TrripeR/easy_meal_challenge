from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    theme = models.CharField(max_length=100, null=True, blank=True)
    required_ingredients = models.CharField(max_length=50)
    max_ingredients = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
