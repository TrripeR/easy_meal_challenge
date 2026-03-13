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
        now = timezone.now()

        if self.is_active and self.end_date < now:
            self.is_active = False
            self.save()


    @classmethod
    def get_active(cls):
        challenge = cls.objects.filter(is_active=True).first()

        if challenge:
            challenge.check_if_expired()

            if not challenge.is_active:
                return None

        return challenge

    def __str__(self):
        return self.title
