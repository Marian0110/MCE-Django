from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'), # Apuntar 127.0.0.1:8000/mce -> a index
    path('index', views.index, name='index'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('accessories', views.accessories, name='accessories'),
    path('coffeeProducts', views.coffeeProducts, name='coffeeProducts'),
    path('history', views.history, name='history'),
    path('loginC', views.loginC, name='loginC'),
    path('register', views.register, name='register'),
    path('logoutC', views.logoutC, name='logoutC'),
]