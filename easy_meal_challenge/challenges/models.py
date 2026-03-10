from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


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

    def clean(self):
        if self.is_active:
            existing = Challenge.objects.filter(is_active=True).exclude(pk=self.pk)

            if existing.exists():
                raise ValidationError("There can be only one active challenge.")

    def check_if_expired(self):

        today = timezone.now().date()

        if self.is_active and self.end_date < today:
            self.is_active = False
            self.save()

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()

    def __str__(self):
        return self.title
