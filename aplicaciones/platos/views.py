from rest_framework import viewsets

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View
from django.shortcuts import render, get_object_or_404, redirect

from .serializers import  PlatosSerializer, PlatosProductosSerializer
from .models import Platos, Platos_productos
from aplicaciones.users.models import Restaurantes
from .forms import EditPlatoForm, createPlatoForm
from aplicaciones.productos.models import Productos



class PlatosViewSet(viewsets.ModelViewSet):
    serializer_class = PlatosSerializer

    def get_queryset(self):
         restaurante = self.request.session.get("restaurante")
         if restaurante:
             return Platos.objects.filter(fk_restaurante_id = restaurante)
         return Platos.objects.all()

class Plato_productosViewSet(viewsets.ModelViewSet):
    serializer_class = PlatosProductosSerializer

    def get_queryset(self):
        id_plato = self.kwargs.get("id_plato")

        restaurante = self.request.session.get("restaurante")
        print ("id restaurante = ", restaurante)
        print(id_plato)
        if restaurante:
            return Platos_productos.objects.filter(fk_restaurante_id = restaurante, fk_plato_id=id_plato)
        return Platos_productos.objects.none()
class adminPlatos(ListView):
    model = Platos
    template_name = "adminPlatos.html"
    context_object_name = "platos"

    def get_queryset(self):
        query = self.request.GET.get("queryBusquedaPlato")
        if query:
            return Platos.objects.filter(nombre_plato__icontains=query, fk_restaurante_id = self.request.session.get("restaurante"))
        return Platos.objects.filter(fk_restaurante_id = self.request.session.get("restaurante"))


class adminPlatosEdit(View):
    template_name = "formularioEditarPlatoAdmin.html"
    success_url = reverse_lazy('adminPlatos')  # Cambia esto según tu URL de éxito
    form_class = EditPlatoForm
    def get(self, request, pk):
        # Obtener el plato que se va a editar
        plato = get_object_or_404(Platos, id=pk)

        # Obtener los productos asociados al plato
        productos_id = list(
            Platos_productos.objects
            .filter(fk_plato=plato)
            .values_list("fk_producto", flat=True)
            .order_by("fk_producto")
        )

        # Convertir los IDs de productos en objetos de productos
        productos_seleccionados = [Productos.objects.get(id=producto_id) for producto_id in productos_id]

        # Obtener todos los productos disponibles
        productos_disponibles = Productos.objects.all().order_by("nombre_producto")

        # Inicializar el formulario con los datos del plato
        form = self.form_class(instance=plato)

        # Pasar el contexto a la plantilla
        context = {
            'form': form,
            'plato': plato,
            'productos_seleccionados': productos_seleccionados,
            'productos_disponibles': productos_disponibles,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        # Obtener el plato que se va a editar
        plato = get_object_or_404(Platos, id=pk)

        # Procesar el formulario enviado
        form = self.form_class(request.POST, instance=plato)

        if form.is_valid():
            # Guardar los datos del formulario en el modelo Platos
            plato = form.save()

            # Obtener los productos seleccionados del formulario
            productos_seleccionados = request.POST.getlist('productos')

            # Eliminar las relaciones anteriores entre el plato y los productos
            Platos_productos.objects.filter(fk_plato=plato).delete()

            # Crear nuevas relaciones entre el plato y los productos seleccionados
            for producto_id in productos_seleccionados:
                producto = get_object_or_404(Productos, id=producto_id)
                Platos_productos.objects.create(fk_plato=plato, fk_producto=producto, fk_restaurante_id=self.request.session["restaurante"] )

            # Redirigir a la URL de éxito
            return redirect(self.success_url)

        # Si el formulario no es válido, volver a mostrar el formulario con errores
        productos_disponibles = Productos.objects.all().order_by("nombre_producto")
        context = {
            'form': form,
            'plato': plato,
            'productos_disponibles': productos_disponibles,
        }
        return render(request, self.template_name, context)

class adminPlatosDelete(DeleteView):
    model = Platos
    template_name = "formularioConfirmDeleteAdmin.html"
    context_object_name = "Platos"
    success_url = reverse_lazy("adminPlatos")


class adminPlatosCreate(CreateView):
    model = Platos
    form_class = createPlatoForm
    template_name = "formularioCrearPlatoAdmin.html"
    success_url = reverse_lazy("adminPlatos")

    def get(self, request):
        form = self.form_class()
        productoss = Productos.objects.all().order_by("nombre_producto")
        return render(request, self.template_name, {"form" : form, "productos_disponibles" : productoss})

    def post(self, request):
        form = self.form_class(request.POST)
        restaurante_id = self.request.session["restaurante"]
        restaurante = Restaurantes.objects.get(id = restaurante_id)
        if form.is_valid():

            nombrePlato = form.cleaned_data["nombre_plato"]
            descripcionPlato = form.cleaned_data["descripcion_plato"]
            precioPlato = form.cleaned_data["precio"]

            plato = Platos.objects.create(nombre_plato = nombrePlato, descripcion_plato = descripcionPlato, precio = precioPlato)
            productos_ids = request.POST.getlist("productos")

            for producto_id in productos_ids:
                productoExiste = Productos.objects.get(id = producto_id)

                Platos_productos.objects.create(fk_plato = plato, fk_producto= productoExiste, fk_restaurante = restaurante)

        else:
            print("Form errors:", form.errors)
            return render(request, self.template_name, {"form": form})
        return redirect(self.success_url)







