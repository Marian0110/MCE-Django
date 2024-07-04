from django.contrib import admin
from mce.models import Cliente, Producto, Accesorio, Historia, Nosotros, Pais
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Accesorio)
admin.site.register(Historia)
admin.site.register(Nosotros)
admin.site.register(Pais)