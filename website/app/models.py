from django.db import models
from django.utils import timezone

# Create your models here.

class Book_info(models.Model):
    #book_id = models.IntegerField()
    name = models.CharField(max_length=10)
    detail = models.CharField(max_length=10, default ='')
    publish_date = models.DateTimeField('date publish', default=timezone.now)

    def __str__(self):
        return self.name


class People_info(models.Model):
    #people_id = models.IntegerField() 
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(Book_info, on_delete=models.CASCADE, default= '')

    def __str__(self):
        return self.name

