from django.db import models

# Create your models here.
class Cliente(models.Model):
    id          = models.AutoField(primary_key=True)
    username    = models.CharField(max_length=20, unique=True, default='default_username', null=False, blank=False)
    email       = models.EmailField(unique=True, max_length=100, blank=False, null=False)
    password    = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    codigo      = models.CharField(max_length=5, default=56) 
    active      = models.BooleanField()

    def __str__(self): #tip:metodo que contiene las clases para mostrar los datos de forma mas determinada cuando se haga la impresion de un objeto en el panel de admin
        return str(self.username)

class Producto(models.Model):
    cod         = models.CharField(unique=True, max_length=5)
    title       = models.CharField(max_length=50, default='default_title')
    price       = models.IntegerField()
    netContent  = models.CharField(max_length=20)
    subtitle    = models.CharField(max_length=200)
    description = models.TextField()
    imagen      = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.cod)+" "+str(self.title)
    
class Accesorio(models.Model):
    cod         = models.CharField(unique=True, max_length=5)
    name        = models.CharField(max_length=40)
    price       = models.IntegerField()
    subtitle    = models.CharField(max_length=200)
    description = models.TextField()
    imagen      = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.cod)+" "+str(self.name)
    
class Historia(models.Model):
    id_historia = models.AutoField(primary_key=True)
    titulo      = models.CharField(max_length=200)
    content     = models.TextField()
    imagen      = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Nosotros(models.Model):
    id          = models.AutoField(primary_key=True)
    titulo      = models.CharField(max_length=100)
    subtitulo   = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen      = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nombre} {self.codigo}"