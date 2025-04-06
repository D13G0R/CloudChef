from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import ListView, View, UpdateView
from rest_framework import viewsets

from aplicaciones.platos.models import Platos
from aplicaciones.productos.models import Productos
from aplicaciones.users.models import Restaurantes

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import pedidos, plato_producto
from .serializers import plato_productoSerializer


# Vista para mostrar la página del mesero
class MeseroView(ListView):
    model = Platos
    template_name = "mesero.html"
    contex_object_name = "Platos"

    def get_queryset(self):
        restaurante_en_session = self.request.session["restaurante"]
        return Platos.objects.filter(fk_restaurante_id = restaurante_en_session)

    #FEATURE DE BUSQUEDA
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        query = self.request.GET.get("queryBusquedaMenu")
        restaurante = self.request.session["restaurante"]
        if query:
            contexto["Productos"] = Productos.objects.filter(nombre_producto__icontains=query)
            contexto["Platos"] = Platos.objects.filter(nombre_plato__icontains=query)  # Agregamos la consulta correctamente
        else:
            contexto["Productos"] = Productos.objects.all().order_by("nombre_producto")
            contexto["Platos"] = Platos.objects.all().order_by("nombre_plato")

        return contexto  # Solo se retorna el diccionario

#creo que esto sobra
# # Logica de busqueda
# @require_GET
# def buscar_items(request):
#     query = request.GET.get('q', '').strip()
#     platos = []
#     productos = []
#
#     if query:
#         # Filtrar platos que coincidan con la consulta
#         platos = list(Platos.objects.filter(nombre_plato__icontains=query).values(
#             'id', 'nombre_plato', 'descripcion_plato', 'precio'
#         ))
#
#         # Filtrar productos que coincidan con la consulta
#         productos = list(Productos.objects.filter(nombre_producto__icontains=query).values(
#             'id', 'nombre_producto', 'descripcion_producto', 'precio_producto'
#         ))
#
#     return JsonResponse({'platos': platos, 'productos': productos})


 # organizacion_platos = {
        #     id_plato :
        #     0-[
        #      0- {producto object_ : stock}
        #      1- {producto object_ : stock}
        #      2- {producto object_ : stock}
        #       ]
        # }
        #organizacion_platos = [
        # {id_plato :
        #   [
        #       {producto object_ : stock}
        #       {producto object_ : stock}
        #   ]
        # }


class ColgarPedido(View):
    def post(self, request, *args, **kwargs):
        platos = request.POST.getlist("plato")  # Lista de nombres de platos
        productos_platos = request.POST.getlist("productoPlato")  # Lista de productos por plato
        productos = request.POST.getlist("producto")  # Productos individuales
        restaurante_id = request.POST.get("restaurante_id")
        print(productos_platos)
        try:
            restaurante = Restaurantes.objects.get(id=restaurante_id)
        except Restaurantes.DoesNotExist:
            return render(request, "error.html", {"error": "Restaurante no encontrado"})

        user = request.user
        if not platos and not productos:
            return render(request, "error.html", {"error": "No se ha seleccionado ningún plato ni producto"})

        # Crear el pedido
        pedido = pedidos.objects.create(fk_usuario=user, estado_pedido="pendiente")

        # Estructura para organizar los platos y sus productos asociados
        organizacion_platos = []

        # Crear un diccionario donde la clave sea el plato con sus productos (para diferenciarlos)
        platos_dict = defaultdict(list)

        for producto_plato in productos_platos:
            platop_id, productop_id = producto_plato.split("-")  # Separar ID del plato y del producto
            producto_existente = Productos.objects.get(id=int(productop_id))

            # Asociamos el producto al plato correspondiente en un diccionario
            platos_dict[platop_id].append(producto_existente)

        for plato_id, productos_asociados in platos_dict.items():
            # Ordenamos los productos para garantizar que la combinación sea única
            productos_asociados = sorted(productos_asociados, key=lambda x: x.id)

            # Revisamos si esta combinación exacta de plato-productos ya existe en nuestra lista
            plato_unico = {
                "plato_id": plato_id,
                "productos": productos_asociados
            }

            if plato_unico not in organizacion_platos:
                organizacion_platos.append(plato_unico)

        # Guardamos los platos y productos en la base de datos
        for registro in organizacion_platos:
            plato_existente = Platos.objects.get(id=int(registro["plato_id"]))

            for producto in registro["productos"]:
                plato_producto.objects.create(
                    fk_pedido=pedido,
                    fk_plato=plato_existente,
                    fk_producto=producto,
                    cantidad=1,
                    fk_restaurante=restaurante
                )

        # Manejo de productos individuales (que no pertenecen a platos)
        lista_productos = defaultdict(int)
        for producto_id in productos:
            lista_productos[producto_id] += 1  # Contamos cuántas veces se repite el producto

        for producto_id, cantidad in lista_productos.items():
            producto_existente = Productos.objects.get(id=int(producto_id))
            plato_producto.objects.create(
                fk_pedido=pedido,
                fk_producto=producto_existente,
                cantidad=cantidad,
                fk_restaurante=restaurante
            )

        return redirect("vistaMesero")


from collections import defaultdict

def vista_cocinero(request):
    restaurante = request.session.get('restaurante')
    pedidos_data = pedidos.objects.filter(fk_restaurante_id = restaurante, estado_pedido = "pendiente").prefetch_related("platos_productos")
    pedidos_procesados = []

    for pedido in pedidos_data:
        plato_dict = defaultdict(list)
        for plato_producto in pedido.platos_productos.all():

            plato = plato_producto.fk_plato.nombre_plato if plato_producto.fk_plato else "Sin Plato"
            producto = plato_producto.fk_producto.nombre_producto
            cantidad = plato_producto.cantidad

            plato_dict[plato].append({
                "producto": producto,
                "cantidad": cantidad
            })

        pedidos_procesados.append({
            "id": pedido.id,
            "estado_pedido": pedido.estado_pedido,
            "platos": dict(plato_dict)
        })
    return render(request, "cocinero.html", {"pedidos": pedidos_procesados})
    # ejemplo de la estructura de los datos
# pedido = [
#     {
#         id: 1,
#         "estado" : "pendiente",
#         "platos" :{
#                 "Tilapia" : [
#                     {"producto": "tilapia"},
#                     {"producto": "arroz blanco"}
#                 ],
#                 "Sierra" : [
#                     {"producto": "Sierra 350"},
#                     {"producto": "arroz blanco"}
#                 ]
#             }
#         ,
#         "sin_plato" : [
#             {"Limonada", "cantidad"},
#             {"Jugo en agua"},
#             {"jugo en leche"}]
#     }
# ]



# Esta es para mostrar los datos con fetch y consumir la api de django
def CocineroView(request):
    return render(request, "cocinero.html", {})

class CocineroViewSet (viewsets.ModelViewSet):
    queryset = plato_producto.objects.all()
    serializer_class = plato_productoSerializer


def DescolgarPedido(request, id):
    pedido = pedidos.objects.get(id = id)
    pedido.estado_pedido = "entregado"
    pedido.save()

    return redirect("vistaCocinero")


def CancelarPedido(request, id):
    pedido = pedidos.objects.get(id = id)
    pedido.estado_pedido = "cancelado"
    pedido.save()
    return redirect("vistaCocinero")























