from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index.html', views.index, name='index'),
    path('404.html', views.error404, name='404'),
    path('blank.html', views.blank, name='blank'),
    path('charts.html', views.charts, name='charts'),
    path('forgot-password.html', views.forgot_password, name='forgot_password'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('tables.html', views.tables, name='tables'),
]