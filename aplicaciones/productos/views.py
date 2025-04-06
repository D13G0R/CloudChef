from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import Productos
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.
class ProductosViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        restaurante = self.request.session.get("restaurante")
        if restaurante:
            return Productos.objects.filter(fk_restaurante = restaurante)
        return Productos.objects.none()

class vistaAyudante(ListView):
    model = Productos
    template_name = "inventario.html"
    context_object_name = "object_list"

    def get_queryset(self):
        query = self.request.GET.get("queryBusquedaProducto")
        if query:
            return Productos.objects.filter(nombre_producto__icontains=query, fk_restaurante_id = self.request.session.get("restaurante"))
        return Productos.objects.filter(fk_restaurante_id = self.request.session.get("restaurante"))
        # return Productos.objects.filter(
        #     Q(nombre_producto__icontains=query) |
        #     Q(descripcion_producto__icontains=query) |
        #     Q(distribuidor_producto__icontains=query)
        # )

class editarProducto(UpdateView):
    model = Productos
    fields = ["nombre_producto", "precio_producto","descripcion_producto", "stock", "distribuidor_producto"]
    success_url = reverse_lazy('vistaAyudante')  # Cambia 'inventario' por el nombre de tu ruta si es diferente.
    template_name = "formularioEditarProducto.html"


class borrarProducto(DeleteView):
    model = Productos
    success_url = reverse_lazy('vistaAyudante')
    template_name = "confirmDeleteUser.html"

class crearProducto(CreateView):
    model = Productos
    fields = ["nombre_producto", "precio_producto","descripcion_producto", "stock", "distribuidor_producto"]
    success_url = reverse_lazy('vistaAyudante')
    template_name = "formularioCrearProducto.html"