from django.contrib import admin

from aplicaciones.users.models import Users, Roles

# Register your models here.
admin.site.register(Users)
admin.site.register(Roles)