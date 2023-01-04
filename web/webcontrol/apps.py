from django.apps import AppConfig
from .tasks import control_loop

class WebcontrolConfig(AppConfig):
    name = 'web'

    def ready(self):
        control_loop()