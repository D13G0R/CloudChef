from django.urls import path
from .views import MeseroView, ColgarPedido, vista_cocinero, DescolgarPedido, CancelarPedido

urlpatterns = [
    path("meseroView/", MeseroView.as_view(), name = "vistaMesero"),
    # path('buscar/', buscar_items, name='buscar_items'),
    path("colgarPedido/", ColgarPedido.as_view(), name ="colgarPedido"),
    path("cocineroView/", vista_cocinero, name = "vistaCocinero"),
    path("descolgarPedido/<int:id>", DescolgarPedido, name = "descolgarPedido"),
    path("cancelarPedido/<int:id>", CancelarPedido, name = "cancelarPedido")
]
