from django.urls import path
from aplicaciones.platos.views import adminPlatos, adminPlatosEdit, adminPlatosDelete, adminPlatosCreate

urlpatterns = [
    path("adminPlatos/", adminPlatos.as_view(), name="adminPlatos"),
    path("adminPlatosAdd/", adminPlatosCreate.as_view(), name="adminPlatosCreate"),
    path("adminPlatosEdit/<int:pk>", adminPlatosEdit.as_view(), name="adminPlatosEdit"),
    path("adminPlatosDelete/<int:pk>", adminPlatosDelete.as_view(), name="adminPlatosDelete"),
]
