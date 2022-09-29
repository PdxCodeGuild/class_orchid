from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

class ChirpsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chirps'