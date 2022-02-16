from django.shortcuts import render

# Create your views here.

def index(request):
    params = {}
    params['nombre_sitio'] = 'Mi Primera App en Django'
    return render(request, 'home/index.html', params)
    
