from django.shortcuts import render

#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#@csrf_exempt
def index(request):
    return render(request, "isc3/index.html")

def error404(request):
    return render(request, "isc3/404.html")

def blank(request):
    return render(request, "isc3/blank.html")

def charts(request):
    return render(request, "isc3/charts.html")

def forgot_password(request):
    return render(request, "isc3/forgot-password.html")

def register(request):
    return render(request, "isc3/register.html")

def tables(request):
    return render(request, "isc3/tables.html")

def login(request):
    return render(request, "isc3/login.html")

def api(request):
    pass
