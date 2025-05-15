# django
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# third
# own
from apps.user.models import Ciudad, Cliente, Cuenta, Movimiento

# Register your models here.

class CiudadResource(resources.ModelResource):
    class Meta:
        model = Ciudad
        import_id_fields = ['codigo_ciudad']

class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('codigo_ciudad', 'nombre_ciudad')
    list_display = ('codigo_ciudad', 'nombre_ciudad', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ['codigo_ciudad', 'nombre_ciudad']
    resource_class = CiudadResource

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        import_id_fields = ['cedula']

class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('cedula', 'rol', 'nombre', 'apellido', 'telefono', 'direccion', 'created_at', 'updated_at')
    list_display = ('cedula', 'usuid', 'rol', 'nombre', 'apellido', 'telefono', 'direccion', 'codigo_ciudad', 'created_at', 'updated_at')
    list_filter = ('rol', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ['cedula']
    resource_class = ClienteResource

class CuentaResource(resources.ModelResource):
    class Meta:
        model = Cuenta
        import_id_fields = ['codigo_cuenta']

class CuentaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('codigo_cuenta', 'nombre_cuenta', 'estado')
    list_display = ('codigo_cuenta', 'nombre_cuenta', 'estado', 'created_at', 'updated_at')
    list_filter = ('cliente', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ['codigo_cuenta']
    resource_class = CuentaResource

class MovimientoResource(resources.ModelResource):
    class Meta:
        model = Movimiento
        import_id_fields = ['id_movimiento']

class MovimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('id_movimiento', 'tipo')
    list_display = ('id_movimiento', 'cliente', 'codigo_cuenta', 'fecha', 'tipo', 'saldo', 'created_at', 'updated_at')
    list_filter = ('fecha', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ['codigo_cuenta']
    resource_class = MovimientoResource

admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Movimiento, MovimientoAdmin)