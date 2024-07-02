from django.shortcuts import render, redirect
from .models import Cliente, Producto, Accesorio, Historia, Nosotros
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    context={}
    return render(request, 'mce/index.html', context)

def aboutUs(request):
    nosotros = Nosotros.objects.all()
    context={'nosotros': nosotros}
    return render(request, 'mce/aboutUs.html', context)

def accessories(request):
    accesorios = Accesorio.objects.all()
    context={'accesorios': accesorios}
    return render(request, 'mce/accessories.html', context)

def coffeeProducts(request):
    productos = Producto.objects.all()
    context={'productos': productos}
    return render(request, 'mce/coffeeProducts.html', context)

def history(request):
    historias = Historia.objects.all()
    id_map = {
        'Hp1': historias[0],
        'Np4_1': historias[1],
        'Np3_1': historias[2],
        'Np4_2': historias[3],
        'Np3_2': historias[4],
        'Np4_3': historias[5],
        'Np3_3': historias[6],
        'Np4_4': historias[7],
    }
    context={'historias': historias, 'id_map': id_map}
    return render(request, 'mce/history.html', context)

def login(request):
    context={}
    return render(request, 'mce/login.html', context)

def register(request):
    context={}
    return render(request, 'mce/register.html', context)