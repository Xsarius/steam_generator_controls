from django.apps import AppConfig
from .tasks import create_controller

class WebcontrolConfig(AppConfig):
    name = 'web'

    def ready(self):
        create_controller()
