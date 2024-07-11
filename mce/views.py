from django.shortcuts import render, redirect
from .models import Cliente, Producto, Accesorio, Historia, Nosotros, Pais
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
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

# def loginC(request):
#     context={}
#     return render(request, 'mce/loginC.html', context)

########### registro/login ############################

def register(request):
    paises = Pais.objects.all()

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass')
        password2 = request.POST.get('verifyPass')
        cel = request.POST.get('phone')
        codigo = request.POST.get('codigoP')

        mensaje = None

        if password1 != password2:
            mensaje = "Las contraseñas no coinciden."
        elif User.objects.filter(username=username).exists():
            mensaje = "El nombre de usuario ya está en uso."
        elif User.objects.filter(email=email).exists():
            mensaje = "El correo ya se encuentra registrado."
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            
            telefono = f"{codigo} {cel}" 

            cliente = Cliente(username=username, email=email, phoneNumber=telefono, password=password2, active=True)
            cliente.save()

            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user)
                mensaje = f"¡Cuenta creada para {username}!"
                return redirect("loginC")
        
        context = {'mensaje': mensaje, 'paises': paises}
        return render(request, 'mce/register.html', context)
    else:
        context = {'paises': paises}
        return render(request, 'mce/register.html', context)

def loginC(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Credenciales correctas')
            request.session['mensaje'] = '¡Inicio de sesión exitoso!'
            request.session['tipo_mensaje'] = 'success'
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            request.session['mensaje'] = 'Nombre de usuario o contraseña incorrectos'
            request.session['tipo_mensaje'] = 'error'
            return render(request, 'mce/loginC.html')
    else:
        return render(request, 'mce/loginC.html')



def logoutC(request):
    logout(request)
    return redirect('index') 

from django.http import JsonResponse

def limpiarMensaje(request):
    if 'mensaje' in request.session:
        del request.session['mensaje']
    if 'tipo_mensaje' in request.session:
        del request.session['tipo_mensaje']
    return JsonResponse({'status': 'ok'})
