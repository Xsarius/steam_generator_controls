from django.shortcuts import render
from django.views import View
from web.wsgi import controller
from webcontrol.tasks import control_loop
from web.celery import debug_task

class Index(View):

    def get(self, request, *args, **kwargs):
        template = 'index.html'

        ht_1_pwr = request.GET.get('heater_1_power')
        ht_2_pwr = request.GET.get('heater_2_power')
        ht_3_pwr = request.GET.get('heater_3_power')
        ht_st_pwr = request.GET.get('heater_steam_power')
        valve = request.GET.get('valve')
        stop = request.GET.get('stop')
        save_toggle = request.GET.get('save')

        commands = {
            'heater_1_power': ht_1_pwr,
            'heater_2_power': ht_2_pwr,
            'heater_3_power': ht_3_pwr,
            'heater_steam_power': ht_st_pwr,
            'valve': valve,
            'STOP': stop,
            'save': save_toggle,
        }

        debug_task().delay()

        controller.set_commands(commands).delay()

        control_loop().delay()

        output = output = {
            'water_temp': 0,
            'steam_temp_1': 0,
            'steam_temp_2': 0,
            'pressure': 0,
            'heater_1': 0,
            'heater_2': 0,
            'heater_3': 0,
            'heater_st': 0,
            'valve': 0,
        }

        context = {
            'output': output,
            'commands': commands
        }

        return render(request, template, context)