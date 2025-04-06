from django.urls import path

from aplicaciones.productos.views import vistaAyudante, editarProducto, borrarProducto, crearProducto

urlpatterns = [
    path("vistaInventario/", vistaAyudante.as_view(), name = "vistaAyudante"),
    path("editarProducto/<int:pk>", editarProducto.as_view(), name = "editarProducto"),
    path("borrarProducto/<int:pk>", borrarProducto.as_view(), name = "borrarProducto"),
    path("crearProducto/", crearProducto.as_view(), name = "crearProducto")
]