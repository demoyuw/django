from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Book_info, People_info

# Create your views here.

'''
def is_working(request):
    return HttpResponse("is wokring!")

def is_working2(request):
    return HttpResponse("is wokring2!")
'''

def index(request):
    #return HttpResponse("Book page")
    get_all = get_object_or_404(Book_info, id=3)
    get_date = str(get_all.publish_date)[:10]
    context = {
        "get_all": get_date
    }
    return render(request, "app/index.html", context)

def detail(request):
    #books = Book_info.objects.get(id=1)
    books = Book_info.objects.all()
    # book_table = get_object_or_404(Book_info)
    context = {
        "book_table": books
    }
    return render(request, "app/detail.html", context)

def results(request, Book_info_id ):
    return HttpResponse("Book result info: %s" % Book_info_id)

def vote(request, Book_info_id ):
    return HttpResponse("Book vote info: %s" % Book_info_id)

