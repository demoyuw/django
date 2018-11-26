from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

from .models import Book_info, People_info

# Create your views here.
@csrf_exempt
def index(request):

    if request.method == "POST":
        user_name = request.POST.get('user_name', None)
        user_password = request.POST.get('user_password', None)
        user = authenticate(username=user_name, password=user_password)
        
        #if user is not None:
        #    login(request, user)
            
        context = {
            "username": user
        } 
        return render(request, "app/index.html", context)
    else:
        context = {
            "username": "GET it's working"
        } 
        return render(request, "app/index.html", context)

def logout_action(request):

        logout(request)
        context = {
            "logout": "yes"
        } 
        return render(request, "app/index.html", context)

def main(request): 
    
    context = {
        
    }
    return render(request, "app/detail.html", context)


def detail(request):
    path = request.path
    method = request.method
    #books = Book_info.objects.get(id=1)
    books = Book_info.objects.all()
    # book_table = get_object_or_404(Book_info)
    # user01 = auth.authenticate(username ='yuwei', password = 'openstack')
    user01 = get_object_or_404(User, pk =1)
    perm_status = user01.has_perm('Book_info')
    book_type = ContentType.objects.get_for_model(Book_info)

    if user01 is not None:
        mss = str(user01.password)
    else:
        mss = "Login fail."
        
    context = {
        "book_table": books,
        "path": path,
        "method": method,
        "mss": mss,
        "perm_status": perm_status,
        #"content_type": str(book_type),
        "request_user": request.user
    }
    return render(request, "app/detail.html", context)

def results(request, Book_info_id ):
    return HttpResponse("Book result info: %s" % Book_info_id)

def vote(request, Book_info_id ):
    return HttpResponse("Book vote info: %s" % Book_info_id)

