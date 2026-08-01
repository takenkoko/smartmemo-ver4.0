from django.apps import AppConfig


class SmartmemoConfig(AppConfig):
    name = 'smartmemo'

    def ready(self):
        import smartmemo.signals