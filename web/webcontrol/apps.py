from django.apps import AppConfig
from .tasks import SGController

sgcontroller1 = SGController()

class WebcontrolConfig(AppConfig):
    name = 'web'

    def ready(self):
        sgcontroller1.control_loop()