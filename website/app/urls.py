from django.urls import path
from .models import Book_info, People_info

from . import views

urlpatterns = [
    #path('check', views.is_working),
    #path('check2', views.is_working2),
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('<int:Book_info_id>/results/', views.results, name='results'),
    path('<int:Book_info_id>/vote/', views.vote, name='vote'),
]