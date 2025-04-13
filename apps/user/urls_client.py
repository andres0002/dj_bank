# django
from django.urls import path
# third
# own
from apps.user.views_client import (
    PerfilCliente, ListadoMovimientos, ListadoCuentas, ListadoCuentasReporte,
    ListadoMovimientosReporte, ListadoMovimientosReporteByDate, ListadoMovimientosReporteByFecha,
    VisualizarCuenta, VisualizarMovimiento, Deposito, Retiro
)

urlpatterns = [
    path('perfil-cliente/', PerfilCliente.as_view(), name='perfil_cliente'),
    path('listar-movimientos/', ListadoMovimientos.as_view(), name='listar_movimientos'),
    path('listar-cuentas/', ListadoCuentas.as_view(), name='listar_cuentas'),

    path('listar-movimientos-reporte/', ListadoMovimientosReporte.as_view(), name='listar_movimientos_reporte'),
    path('listar-cuentas-reporte/', ListadoCuentasReporte.as_view(), name='listar_cuentas_reporte'),
    path('listar-movimientos-by-fecha/<int:id_usr>/', ListadoMovimientosReporteByDate.as_view(), name='listar_movimientos_by_fecha'),
    path('listar-movimientos-por-fecha/', ListadoMovimientosReporteByFecha.as_view(), name='listar_movimientos_por_fecha'),

    path('visualizar-cuentas/<int:id_codigo_cuenta>/', VisualizarCuenta.as_view(), name='visualizar_cuenta'),
    path('visualizar-movimientos/<int:id_movimiento>/', VisualizarMovimiento.as_view(), name='visualizar_movimientos'),
    path('realizar-deposito/<int:id_cuenta>/', Deposito.as_view(), name='realizar_deposito'),
    path('realizar-retiro/<int:id_cuenta>/', Retiro.as_view(), name='realizar_retiro'),
]