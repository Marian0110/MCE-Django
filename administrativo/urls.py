from django.urls import path
from . import views

urlpatterns=[
    path('crud', views.crud, name='crud'),
    path('crudProductos', views.crudProductos, name='crudProductos'),
    path('crudAccesorios', views.crudAccesorios, name='crudAccesorios'),
    path('crudHistorias', views.crudHistorias, name='crudHistorias'),
    path('crudNosotros', views.crudNosotros, name='crudNosotros'),
    path('crudClientes', views.crudClientes, name='crudClientes'),

    path('registro', views.registro, name='registro'),

    path('agregarSobreN', views.agregarSobreN, name='agregarSobreN'),
    path('eliminarN/<id>', views.eliminarN, name='eliminarN'),
    path('editarN', views.editarN, name='editarN'),
    path('edicionN/<id>', views.edicionN, name='edicionN'),

    path('agregarProducto', views.agregarProducto, name='agregarProducto'),
    path('edicionProducto/<cod>', views.edicionProducto, name='edicionProducto'),
    path('editarProducto', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<cod>', views.eliminarProducto, name='eliminarProducto'),
    
    path('agregarAccesorio', views.agregarAccesorio, name='agregarAccesorio'),
    path('edicionAccesorio/<cod>', views.edicionAccesorio, name='edicionAccesorio'),
    path('editarAccesorio', views.editarAccesorio, name='editarAccesorio'),
    path('eliminarAccesorio/<cod>', views.eliminarAccesorio, name='eliminarAccesorio'),

    path('agregarHistoria', views.agregarHistoria, name='agregarHistoria'),
    path('edicionHistoria/<id_historia>', views.edicionHistoria, name='edicionHistoria'),
    path('editarHistoria', views.editarHistoria, name='editarHistoria'),
    path('eliminarHistoria/<id_historia>', views.eliminarHistoria, name='eliminarHistoria'),
    
    path('agregarCliente', views.agregarCliente, name='agregarCliente'),
    path('eliminarCliente/<id>', views.eliminarCliente, name='eliminarCliente'),
    path('edicionCliente/<id>', views.edicionCliente, name='edicionCliente'),
    path('editarCliente', views.editarCliente, name='editarCliente'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
]

