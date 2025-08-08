from django.apps import AppConfig
import mongoengine


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

    def ready(self):
        mongoengine.connect(
            db="polls_db",
            host="localhost",
            port = 27017
        )