from django.apps import AppConfig
from .tasks import SGController

class WebcontrolConfig(AppConfig):
    name = 'web'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.controller = SGController()

    def ready(self):
        self.controller.control_loop()