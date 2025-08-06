from django.apps import AppConfig
from mongoengine import connect


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

    def ready(self):
        connect(
            db="polls_db",
            host="localhost",
            port = 27017
        )