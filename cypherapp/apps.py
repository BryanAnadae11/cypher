from django.apps import AppConfig


class CypherappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cypherapp'

    def ready(self):
    	import cypherapp.signals
