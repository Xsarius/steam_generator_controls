from django.shortcuts import render

# Create your views here.
def index(request):
    print(print('Temperature: {0:0.3f}C'.format(1)))
    return render(request, 'Home.html', {'text': 1})