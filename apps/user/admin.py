# django
from django.contrib import admin
# third
# own
from apps.user.models import Ciudad, Cliente, Cuenta, Movimiento

# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Movimiento)