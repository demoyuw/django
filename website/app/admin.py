from django.contrib import admin
from .models import Book_info, People_info

# Register your models here.
admin.site.register(Book_info)
admin.site.register(People_info)