from django.apps import AppConfig
from .tasks import sgcontroller1

class WebcontrolConfig(AppConfig):
    name = 'web'

    def ready(self):
        sgcontroller1.control_loop()