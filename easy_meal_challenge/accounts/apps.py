from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'easy_meal_challenge.accounts'

    def ready(self):
        import easy_meal_challenge.accounts.signals
