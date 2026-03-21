from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

from easy_meal_challenge.accounts.validators import first_name_min_length_validator, first_letter_upper_case, \
    last_name_min_length_validator


# Create your models here.

class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=100)
    users = models.ManyToManyField(User,blank=True,related_name="badges")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            first_name_min_length_validator,
            first_letter_upper_case
        ],
        help_text="First name can not be shorter than 3 letters or longer than 20 letters",
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            MaxLengthValidator(20),
            last_name_min_length_validator,
            first_letter_upper_case
        ],
        help_text="Last name can not be shorter than 2 letters or longer than 20 letters",
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(120),
            MinValueValidator(7),
        ],
        help_text="Age must be higher then 7 years old",
    )
    cooking_exp = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Tell us a bit about your cooking experiences",
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username




