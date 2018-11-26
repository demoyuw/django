from django.urls import path
from .models import Book_info, People_info

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout_action, name='logout_action'),  
    path('main', views.main, name='main'),   
     
    path('detail', views.detail, name='detail'),
    path('<int:Book_info_id>/results/', views.results, name='results'),
    path('<int:Book_info_id>/vote/', views.vote, name='vote'),
]