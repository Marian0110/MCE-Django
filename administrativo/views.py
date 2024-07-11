from django.shortcuts import render, redirect
from mce.models import Cliente, Producto, Accesorio, Historia, Nosotros, Pais
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import paisForm
########  LOGIN/REGISTRO ADMIN ##########
@login_required
def registro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

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
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user)
                mensaje = f"¡Cuenta creada para {username}!"
                return redirect("login") 

        context = {'mensaje': mensaje}
        return render(request, "registration/registro.html", context)
    
    return render(request, "registration/registro.html")

########################################################

########## CRUDS ################################
@login_required
def crud(request):
    clientes = Cliente.objects.all()
    nosotros = Nosotros.objects.all()
    productos = Producto.objects.all()
    accesorios = Accesorio.objects.all()
    historias = Historia.objects.all()
    return render(request, 'administrativo/crud.html', {'clientesTotales': clientes, 'nosotros': nosotros, 'productosTotales': productos, 'accesoriosTotales': accesorios, 'historias': historias,})

@login_required
def crudClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'administrativo/crudClientes.html', {'clientesTotales': clientes})

@login_required
def crudProductos(request):
    productos = Producto.objects.all()
    contxto={'productosTotales': productos}
    return render(request, 'administrativo/crudProductos.html', contxto)

@login_required
def crudHistorias(request):
    historias = Historia.objects.all()
    context={'historias' : historias}
    return render(request, 'administrativo/crudHistorias.html', context)

@login_required
def crudAccesorios(request):
    accesorios = Accesorio.objects.all()
    context={'accesoriosTotales' : accesorios}
    return render(request, 'administrativo/crudAccesorios.html', context)

@login_required
def crudNosotros(request):
    nosotros = Nosotros.objects.all()
    context={'nosotros' : nosotros}
    return render(request, 'administrativo/crudNosotros.html', context)
#####################################################
@login_required
def crud_paises(request):
    paises= Pais.objects.all()
    context={"paises":paises}
    
    return render(request, 'administrativo/paises_list.html', context)

@login_required
def paisesAdd(request):
    context={}
    if request.method == "POST":
        form = paisForm(request.POST)
        if form.is_valid():
            form.save()
            form=paisForm()
            context={'mensaje': "OK, Datos grabados...","form":form}
            return render(request, "administrativo/paises_add.html",context)
    
    else:
        form = paisForm()
        context={'form':form}
        return render(request,'administrativo/paises_add.html',context)

@login_required    
def paises_del(request, pk):
    context={}
    try:
        pais= Pais.objects.get(pk=pk)
        pais.delete()
        mensaje= "Datos eliminados con exito"
        paises= Pais.objects.all()
        context={'paises':paises, 'mensaje': mensaje}
        return render(request, 'administrativo/paises_list.html', context)
    except:
        mensaje= "Pais no encontrado."
        paises= Pais.objects.all()
        context={'paises':paises, 'mensaje': mensaje}
        return render(request, 'administrativo/paises_list.html', context)

@login_required    
def paises_edit(request,pk):
    context={}
    try:
        pais= Pais.objects.get(pk=pk)
        if pais:
            if request.method == "POST":
                form=paisForm(request.POST,instance=pais)
                form.save()
                form=paisForm()
                mensaje="Bien, datos actualizados..."
                context={'pais':pais, 'mensaje': mensaje, 'form' : form}
                return render(request, 'administrativo/paises_edit.html', context)
            else:
                form = paisForm(instance=pais)
                mensaje = ""
                context={'pais':pais, 'form':form,'mensaje': mensaje}
                return render(request, 'administrativo/paises_edit.html', context)
    except:
        paises= Pais.objects.all()
        mensaje = "Error, id no existe."
        context={'paises':paises, 'mensaje': mensaje}
        return render(request, 'administrativo/paises_list.html', context)
#####################################################################################

@login_required
def agregarProducto(request):
    mensaje = None
    if request.method == "POST":
        codigo = request.POST["cod"]
        titulo = request.POST["title"]
        subtitulo = request.POST["sub"]
        precio = request.POST['price']
        contenidoN = request.POST["cont"]
        desc = request.POST["desc"]
        imagen = request.FILES.get('img')
    
        producto_nuevo = Producto.objects.create(
                cod=codigo,
                title=titulo,
                subtitle=subtitulo,
                price=precio,
                netContent=contenidoN,
                description=desc,
                imagen=imagen
            )
        producto_nuevo.save()
        mensaje = "Datos guardados correctamente"
        productosTotales = Producto.objects.all()
        context = {'productosTotales': productosTotales, 'mensaje': mensaje}
        return render(request, 'administrativo/crudProductos.html', context)
    else:
        return redirect('crudProductos')

@login_required
def edicionProducto(request, cod):
    producto= Producto.objects.get(cod=cod)
    context= {'producto': producto}
    return render(request, 'administrativo/edicionProducto.html', context)

@login_required
def editarProducto(request):
    if request.method == "POST":
        codigo = request.POST["cod"]
        titulo = request.POST["title"]
        subtitulo = request.POST["sub"]
        precio = request.POST["price"]
        contenidoN = request.POST["cont"]
        desc = request.POST["desc"]
        imagen = request.FILES.get('img')

        producto = Producto.objects.get(cod=codigo)
        producto.title = titulo
        producto.subtitle = subtitulo
        producto.price = precio
        producto.netContent = contenidoN
        producto.description = desc
        if imagen:
            producto.imagen = imagen

        producto.save()
        mensaje = "Datos actualizados correctamente"
        contexto = {'mensaje': mensaje, 'producto': producto}
        return render(request, 'administrativo/edicionProducto.html', contexto)
    else:
        return render(request, 'administrativo/edicionProducto.html')

@login_required
def eliminarProducto(request, cod):
    producto_eliminado= Producto.objects.get(cod=cod)
    producto_eliminado.delete()
    return redirect('crudProductos')

@login_required
def agregarAccesorio(request):
    if request.method == "POST":
        codigo = request.POST["cod"]
        titulo = request.POST["name"]
        subtitulo = request.POST["sub"]
        precio = request.POST['price']
        desc = request.POST["desc"]
        imagen = request.FILES.get('img')
    
        accesorio_nuevo = Accesorio.objects.create(
                cod=codigo,
                name=titulo,
                subtitle=subtitulo,
                price=precio,
                description=desc,
                imagen=imagen
            )
        accesorio_nuevo.save()
        mensaje = "Datos guardados correctamente"
        accesoriosTotales = Accesorio.objects.all()
        context = {'accesoriosTotales': accesoriosTotales, 'mensaje': mensaje}
        return render(request, 'administrativo/crudAccesorios.html', context)
    else:
        return redirect('crudAccesorios')

@login_required
def edicionAccesorio(request, cod):
    accesorio= Accesorio.objects.get(cod=cod)
    context= {'accesorio': accesorio}
    return render(request, 'administrativo/edicionAccesorio.html', context)

@login_required
def editarAccesorio(request):
    if request.method == "POST":
        codigo = request.POST["cod"]
        titulo = request.POST["name"]
        subtitulo = request.POST["sub"]
        precio = request.POST["price"]
        desc = request.POST["desc"]
        imagen = request.FILES.get('img')

        accesorio = Accesorio.objects.get(cod=codigo)
        accesorio.name = titulo
        accesorio.subtitle = subtitulo
        accesorio.price = precio
        accesorio.description = desc
        if imagen:
            accesorio.imagen = imagen

        accesorio.save()
        mensaje = "Datos actualizados correctamente"
        contexto = {'mensaje': mensaje, 'accesorio': accesorio}
        return render(request, 'administrativo/edicionAccesorio.html', contexto)
    else:
        return render(request, 'administrativo/edicionAccesorio.html')

@login_required
def eliminarAccesorio(request, cod):
    accesorio_eliminado= Accesorio.objects.get(cod=cod)
    accesorio_eliminado.delete()
    return redirect('crudAccesorios')

@login_required
def agregarHistoria(request):
    if request.method == "POST":
        titulo = request.POST["title"]
        contenido = request.POST["content"]
        imagen = request.FILES.get('img')
    
        historia_nueva = Historia.objects.create(
                titulo=titulo,
                content=contenido,
                imagen=imagen
            )
        historia_nueva.save()
        mensaje = "Datos guardados correctamente"
        historias = Historia.objects.all()
        context = {'historias': historias, 'mensaje': mensaje}
        return render(request, 'administrativo/crudHistorias.html', context)
    else:
        return redirect('crudHistorias')

@login_required
def edicionHistoria(request, id_historia):
    historia= Historia.objects.get(id_historia=id_historia)
    context= {'historia': historia}
    return render(request, 'administrativo/edicionHistoria.html', context)

@login_required
def editarHistoria(request):
    if request.method == "POST":
        id = request.POST["identifier"]
        titulo = request.POST["title"]
        contenido = request.POST["content"]
        imagen = request.FILES.get('img')

        historia = Historia.objects.get(id_historia=id)
        historia.titulo = titulo
        historia.content = contenido
        if imagen:
            historia.imagen = imagen

        historia.save()
        mensaje = "Datos actualizados correctamente"
        contexto = {'mensaje': mensaje, 'historia': historia}
        return render(request, 'administrativo/edicionHistoria.html', contexto)
    else:
        historia = Historia.objects.get(id_historia=id)
        contexto = {'historia': historia}
        return render(request, 'administrativo/edicionHistoria.html', contexto)

@login_required
def eliminarHistoria(request, id_historia):
    historia_eliminada= Historia.objects.get(id_historia=id_historia)
    historia_eliminada.delete()
    return redirect('crudHistorias')

@login_required
def agregarCliente(request):
    nomUser = request.POST["user"]
    email = request.POST["email"]
    pas = request.POST["pass"]
    cel = request.POST["cel"]
    activo = "1"
    
    cliente_nuevo = Cliente.objects.create(
                username=nomUser,
                email=email,
                password=pas,
                phoneNumber=cel,
                active=activo
            )
    cliente_nuevo.save()
    return redirect(reverse('crud'))
    
@login_required
def eliminarCliente(request, id):
    cliente= Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('../crudClientes')
    
@login_required
def edicionCliente(request, id):
    cliente= Cliente.objects.get(id=id)
    context= {'cliente': cliente}
    return render(request, 'administrativo/edicionCliente.html', context)

@login_required
def editarCliente(request):
    if request.method == "POST":
        cliente_id = request.POST['identifier']
        user = request.POST['user']
        pas = request.POST['pass']
        email_nuevo = request.POST['email']
        cel = request.POST['cel']
        activo = "1"

        cliente = Cliente.objects.get(id=cliente_id)
        cliente.username = user
        cliente.password = pas
        cliente.email = email_nuevo
        cliente.phoneNumber = cel
        cliente.active = activo

        if Cliente.objects.filter(email=email_nuevo).exclude(id=cliente_id).exists():
            context = {'cliente': cliente, 'error': 'El correo electrónico ya está en uso'}
            return render(request, 'administrativo/editarCliente.html', context)

        cliente.save()
        mensaje = "Datos actualizados correctamente"
        contexto = {'mensaje': mensaje, 'cliente': cliente}
        return render(request, 'administrativo/edicionCliente.html', contexto)
    else:
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'administrativo/edicionCliente.html')

@login_required
def clientesUpdate(request):
    if request.method == "POST":
        cliente_id=request.POST['identifier']
        user=request.POST['user']
        pas=request.POST['pass']
        email_nuevo=request.POST['email']
        cel=request.POST['cel']
        activo="1"
            
        cliente = Cliente()
        cliente.id=cliente_id
        cliente.username=user
        cliente.password=pas
        cliente.email=email_nuevo
        cliente.phoneNumber=cel
        cliente.active=activo
        cliente.save()

        if cliente.email != email_nuevo:
            if Cliente.objects.filter(email=email_nuevo).exclude(id=cliente_id).exists():
                context = {'cliente': cliente, 'error': 'El correo electrónico ya está en uso por otro cliente.'}
                return render(request, 'administrativo/clientes_edit.html', context)

        context={'mensaje': "Datos actualizados correctamente", 'cliente':cliente}
        return render(request, 'administrativo/clientes_edit.html', context)
    else:
        #no post
        clientes = Cliente.objects.all()
        context={'clientes':clientes}
        return render(request, 'administrativo/clientes_edit.html', context)

@login_required
def agregarSobreN(request):
    mensaje = None
    if request.method == "POST":
        titulo = request.POST["title"]
        subtitulo = request.POST["sub"]
        desc = request.POST["desc"]
        imagen = request.FILES.get('img')

        nosotros = Nosotros.objects.create(
            titulo=titulo,
            subtitulo=subtitulo,
            descripcion=desc,
            imagen=imagen
        )
        nosotros.save()
        mensaje = "Datos guardados correctamente"
        nosotros = Nosotros.objects.all()
        context = {'nosotros': nosotros, 'mensaje': mensaje}
        return render(request, 'administrativo/crudNosotros.html', context)
    else:
        return redirect('crudNosotros')

@login_required
def eliminarN(request, id):
    nosotros= Nosotros.objects.get(id=id)
    nosotros.delete()
    return redirect('crudNosotros')

@login_required
def editarN(request):
    if request.method == "POST":
        id = request.POST["identifier"]
        titulo = request.POST["title"]
        subtitulo = request.POST["sub"]
        desc = request.POST["desc"]
        imagen = request.FILES.get('img')

        nosotros = Nosotros.objects.get(id=id)
        nosotros.titulo = titulo
        nosotros.subtitulo = subtitulo
        nosotros.descripcion = desc
        if imagen:
            nosotros.imagen = imagen

        nosotros.save()
        mensaje = "Datos actualizados correctamente"
        contexto = {'mensaje': mensaje, 'nosotros': nosotros}
        return render(request, 'administrativo/edicionN.html', contexto)
    else:
        return redirect('crudNosotros')

@login_required
def edicionN(request, id):
    nosotros = Nosotros.objects.get(id=id)
    context= {'nosotros': nosotros}
    return render(request, 'administrativo/edicionN.html', context)
