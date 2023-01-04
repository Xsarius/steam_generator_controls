from django.apps import AppConfig
from .tasks import SGController

class WebcontrolConfig(AppConfig):
    name = 'web'

    def ready(self):
        SGController.control_loop()