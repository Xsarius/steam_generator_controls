from django.apps import AppConfig
from .tasks import SGController

class WebcontrolConfig(AppConfig):
    name = 'web'

    def __init__(self, app_name, app_module):
        super(WebcontrolConfig, self).__init__(app_name, app_module)
        self.controller = None

    def ready(self):
        if self.controller is None:
            self.controller = SGController()
        self.controller.control_loop()
