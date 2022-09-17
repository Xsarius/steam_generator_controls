from django.shortcuts import render
from .rpi import temp1

# Create your views here.
def index(request):
    print(print('Temperature: {0:0.3f}C'.format(temp1.getTemp())))
    return render(request, 'index.html', {'text': temp1.getTemp()})