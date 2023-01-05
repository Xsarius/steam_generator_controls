from django.shortcuts import render
from django.views import View
from web.wsgi import controller

class Index(View):

    def get(self, request, *args, **kwargs):
        template = 'index.html'

        emergerny_stop = request.GET.get('emergency_stop')

        if(emergerny_stop):
            pass

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

        controller.set_commands(commands)

        output = controller.get_output()

        return render(request, template)