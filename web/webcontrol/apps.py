from django.apps import AppConfig
from web.wsgi import controller

class WebcontrolConfig(AppConfig):
    name = 'web'

    def ready(self):
        controller.control_loop()
