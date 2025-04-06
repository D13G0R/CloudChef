"""
URL configuration for restaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from restaurante.views import home, presentacion
from django.contrib.auth import views as auth_views
from aplicaciones.pedidos.views import CocineroViewSet
from aplicaciones.platos.views import PlatosViewSet, Plato_productosViewSet

from aplicaciones.productos.views import ProductosViewSet

router = routers.DefaultRouter()
# router.register("platoProductos", PlatosViewSet, basename="platos") # esta se usaba cuando la tabla de muchos a muchos fue creada automaticamente pero como tenia que agregar la tabla manualmente toca hacerlo manualmente todo
router.register("productosPlato", ProductosViewSet, basename="productos")
router.register("pedidoCocina", CocineroViewSet, basename="pedidos")
# router.register(r"platoProductos/<str:id_plato>", Plato_productosViewSet, basename="plato_productos")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name ="home"),
    path("presentacion/", presentacion, name ="presentacion"),
    path("users/", include('aplicaciones.users.urls')),
    path("pedidos/", include('aplicaciones.pedidos.urls')),
    path("platos/", include('aplicaciones.platos.urls')),
    path("productos/", include('aplicaciones.productos.urls')),
    path('api/platoProductos/<int:id_plato>/', Plato_productosViewSet.as_view({'get': 'list'}), name='plato_productos'),
    path("api/", include(router.urls)),

    # Vista para solicitar recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #
    # Confirmación de que el correo fue enviado
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # Página para establecer una nueva contraseña
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Confirmación de que la contraseña se cambió correctamente
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
