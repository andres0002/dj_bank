# django
from django.urls import path
# third
# own
from apps.user.views_admin import (
    ListadoClientes, ListadoClientesReporte, AdicionarCliente, AdicionarCuenta,
    VisualizarCliente, ModificarCliente, BorrarCliente, VisualizarCuenta,
    ModificarCuenta, BorrarCuenta, PerfilAdministrador, ListadoCuentas,
    ListadoCuentasReporte, ListadoMovimientosReporteByDate, ListadoMovimientosReporteByFecha,
    ListadoMovimientos, ListadoMovimientosGeneral, ListadoMovimientosReporte,
    ListadoCuentasReporteCliente, VisualizarClienteHipervinculo, VisualizarClienteCuentaHipervinculo,
    VisualizarMovimiento
)

urlpatterns = [
    path('listar-clientes/', ListadoClientes.as_view(), name='listar_clientes'),
    path('listar-clientes-reporte/', ListadoClientesReporte.as_view(), name='listar_clientes_reporte'),
    path('adicionar-cliente/', AdicionarCliente.as_view(), name='adicionar_cliente'),
    path('visualizar-cliente/<int:id_cliente>/', VisualizarCliente.as_view(), name='visualizar_cliente'),
    path('modificar-cliente/<int:id_cliente>/', ModificarCliente.as_view(), name='modificar_cliente'),
    path('borrar-cliente/<int:id_cliente>/', BorrarCliente.as_view(), name='borrar_cliente'),
    path('lista-cuentas/', ListadoCuentas.as_view(), name='listar_cuentas'),
    path('lista-cuentas-reporte/', ListadoCuentasReporte.as_view(), name='listar_cuentas_reporte'),
    path('adicionar-cuenta/', AdicionarCuenta.as_view(), name='adicionar_cuenta'),
    path('visualizar-cuenta/<int:id_codigo_cuenta>/', VisualizarCuenta.as_view(), name='visualizar_cuenta'),
    path('visualizar-movimiento/<int:id_movimiento_visualizar>/', VisualizarMovimiento.as_view(), name='visualizar_movimientos'),
    path('modificar-cuenta/<int:id_codigo_cuenta>/', ModificarCuenta.as_view(), name='modificar_cuenta'),
    path('borrar-cuenta/<int:id_codigo_cuenta>/', BorrarCuenta.as_view(), name='borrar_cuenta'),
    path('perfil-admin/', PerfilAdministrador.as_view(), name='perfil_administrador'),

    path('listar-movimientos-by-fecha/<int:id_cuen>/', ListadoMovimientosReporteByDate.as_view(), name='listar_movimientos_by_fecha'),
    path('listar-movimientos-por-fecha/', ListadoMovimientosReporteByFecha.as_view(), name='listar_movimientos_por_fecha'),
    path('listar-movimientos/', ListadoMovimientos.as_view(), name='listar_movimientos'),
    path('listar-movimientos-general/', ListadoMovimientosGeneral.as_view(), name='listar_movimientos_general'),
    path('listar-movimientos-reporte/', ListadoMovimientosReporte.as_view(), name='listar_movimientos_reporte'),
    path('listar-cuentas-por-cliente/<int:id_c>/', ListadoCuentasReporteCliente.as_view(), name='listar_cuentas_reporte_cliente'),

    path('visualizar-cliente-hipervinculo/<int:id_cliente>/', VisualizarClienteHipervinculo.as_view(), name='visualizar_cliente_hipervinculo'),
    path('visualizar-cuenta-cliente-hipervinculo/<int:id_cliente>/', VisualizarClienteCuentaHipervinculo.as_view(), name='visualizar_cuenta_cliente_hipervinculo'),
]