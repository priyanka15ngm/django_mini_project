from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #after making signals.py
    def ready(self):
        import users.signals
