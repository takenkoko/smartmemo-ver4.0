from django.apps import AppConfig


class SmartmemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smartmemo'

    def ready(self):
        import smartmemo.signals