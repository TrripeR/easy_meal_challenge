from django.contrib import admin

from easy_meal_challenge.accounts.models import Profile, Badge


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name',)