from django.contrib import admin
from .models import Book_info, People_info


class bookAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish_date')


# Register your models here.
admin.site.register(Book_info, bookAdmin)
admin.site.register(People_info)


