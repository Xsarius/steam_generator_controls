from django.http import HttpResponse
from django.views import View
from ..sensors import sensors
from ..web.settings import PINS

pt100 = sensors.Pt100_SPI(PINS['TEMP_WATER_1'])

class Index(View):
    def get(self, request):
        return HttpResponse(pt100.getTemp())
