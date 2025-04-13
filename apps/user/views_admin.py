# -*- coding: utf-8 -*-
# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth.models import User
# third
# own
from apps.user.models import Cliente, Ciudad, Cuenta, Movimiento
from apps.user.forms import AdicionarClienteForm, ClienteForm, CuentaForm, MovimientoForm

class PerfilAdministrador(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/perfil_administrador.html'
    form_class = ClienteForm

    def get(self, request):
        try:
            datos_usuario = Cliente.objects.get(usuid=request.user.pk)
            form = self.form_class(instance=datos_usuario)
            return render(request, self.template_name, {'form': form})

        except Cliente.DoesNotExist:
            return render(request, "page_404.html")

    def post(self, request):
        try:
            datos_usuario = Cliente.objects.get(usuid=request.user.pk)
            form = self.form_class(request.POST, instance=datos_usuario)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'El Perfil se modificó correctamente')

                listar = ListadoClientes()
                return listar.get(request)

            else:
                messages.add_message(request, messages.ERROR, 'El Perfil no se pudo modificar')

            listar = ListadoClientes()
            return listar.get(request)

        except Cliente.DoesNotExist:
            return render(request, "page_404.html")

class ListadoClientes(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_clientes.html'
    form_class = ClienteForm

    def get(self, request):
        lista_clientes = Cliente.objects.all()
        return render(request, self.template_name, {'clientes': lista_clientes})

class ListadoClientesReporte(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_clientes_reporte.html'
    form_class = ClienteForm

    def get(self, request):
        lista_clientes = Cliente.objects.all()
        return render(request, self.template_name, {'clientes': lista_clientes})

class ListadoCuentas(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_cuentas.html'

    def get(self, request):
        lista_cuentas = Cuenta.objects.all()
        return render(request, self.template_name, {'cuentas': lista_cuentas})

class ListadoCuentasReporte(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_cuentas_reporte.html'

    def get(self, request):
        lista_cuentas = Cuenta.objects.all()
        return render(request, self.template_name, {'cuentas': lista_cuentas})

class ListadoCuentasReporteCliente(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_cuentas_reporte_cliente.html'

    def get(self, request, id_c):
        lista_cunetas = Cuenta.objects.filter(cliente=id_c)
        return render(request, self.template_name, {'cuentas': lista_cunetas})

class AdicionarCliente(LoginRequiredMixin, View):
    login_url = '/'
    form_class = AdicionarClienteForm
    template_name = 'admin/adicionar_cliente.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        cedula = request.POST.get('cedula', None)
        nombres = request.POST.get('nombre', None)
        apellidos = request.POST.get('apellido', None)
        telefono = request.POST.get('telefono', None)
        direccion = request.POST.get('direccion', None)
        codigo_ciudad = request.POST.get('nombre_ciudad', None)
        rol = request.POST.get('rol', None)

        if password == confirm_password:
            if username and email and password and confirm_password:
                user, created = User.objects.get_or_create(
                    username=username,
                    email=email,
                    first_name=nombres,
                    last_name=apellidos
                )

                if created:
                    try:
                        user.set_password(password)
                        user.save()
                        ciudad = Ciudad.objects.get(codigo_ciudad=codigo_ciudad)
                        cliente = Cliente(
                            cedula=cedula,
                            nombre=nombres,
                            apellido=apellidos,
                            telefono=telefono,
                            direccion=direccion,
                            codigo_ciudad=ciudad,
                            rol=rol,
                            usuid=user
                        )
                        cliente.save()
                        messages.add_message(request, messages.INFO, "El cliente se agrego satisfactoriamente")
                        list = ListadoClientes()
                        return list.get(request)

                    except Ciudad.DoesNotExist:
                        messages.add_message(request, messages.ERROR, "No existe la ciudad")

                else:
                    messages.add_message(request, messages.ERROR, "El usuario ya existe en el sistema")

            else:
                messages.add_message(request, messages.ERROR, "Faltan campos por llenar en el formulario")

        else:
            messages.add_message(request, messages.ERROR, "Verique las contraseña")

        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

class VisualizarCliente(LoginRequiredMixin, View):
    login_url = '/'
    form_class = ClienteForm
    template_name = 'admin/visualizar_cliente.html'

    def get(self, request, id_cliente):
        cedula_cliente = Cliente.objects.get(cedula=id_cliente)
        form = self.form_class(instance=cedula_cliente)
        return render(request, self.template_name, {'form': form})

class VisualizarClienteHipervinculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = ClienteForm
    template_name = 'admin/visualizar_cliente_hipervinculo.html'

    def get(self, request, id_cliente):
        cedula_cliente = Cliente.objects.get(cedula=id_cliente)
        form = self.form_class(instance=cedula_cliente)
        return render(request, self.template_name, {'form': form})

class VisualizarClienteCuentaHipervinculo(LoginRequiredMixin, View):
    login_url = '/'
    form_class = ClienteForm
    template_name = 'admin/visualizar_cuenta_cliente_hipervinculo.html'

    def get(self, request, id_cliente):
        cliente = Cliente.objects.get(cedula=id_cliente)
        form = self.form_class(instance=cliente)
        return render(request, self.template_name, {'form': form})

class ModificarCliente(LoginRequiredMixin, View):
    login_url = '/'
    form_class = ClienteForm
    template_name = 'admin/modificar_cliente.html'

    def get(self, request, id_cliente):
        cedula_cliente = Cliente.objects.get(cedula=id_cliente)
        form = self.form_class(instance=cedula_cliente)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id_cliente):
        cedula_cliente = Cliente.objects.get(cedula=id_cliente)
        form = self.form_class(request.POST, instance=cedula_cliente)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El Cliente se modificó correctamente')
            listar = ListadoClientes()
            return listar.get(request)

        else:
            messages.add_message(request, messages.ERROR, 'El Cliente no se pudo modificar')

        listar = ListadoClientes()
        return listar.get(request)

class BorrarCliente(LoginRequiredMixin, View):
    login_url = '/'
    form_class = ClienteForm
    template_name = 'admin/borrar_cliente.html'

    def get(self, request, id_cliente):
        try:
            cedula_cliente = Cliente.objects.get(cedula=id_cliente)
            form = self.form_class(instance=cedula_cliente)
            return render(request, self.template_name, {'form': form})

        except Cliente.DoesNotExist:
            listar = ListadoClientes()
            return listar.get(request)

    def post(self, request, id_cliente):
        cedula_cliente = Cliente.objects.get(cedula=id_cliente)
        cedula_cliente.delete()
        messages.add_message(request, messages.INFO, "El cliente se borró correctamente")

        listar = ListadoClientes()
        return listar.get(request)

class AdicionarCuenta(LoginRequiredMixin, View):
    login_url = '/'
    form_class = CuentaForm
    template_name = 'admin/adicionar_cuenta.html'

    def get(self, request):
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        try:
            form = self.form_class(request.POST)

            if form.is_valid:
                form.save()
                messages.add_message(request, messages.INFO, 'La Cuenta se adicionó correctamente')

            else:
                messages.add_message(request, messages.ERROR, 'La Cuenta no se pudo adicionar')

        except Cuenta.DoesNotExist:
            return render(request, "page_404.html")

        listar = ListadoCuentas()
        return listar.get(request)

class VisualizarCuenta(LoginRequiredMixin, View):
    login_url = '/'
    form_class = CuentaForm
    template_name = 'admin/visualizar_cuenta.html'

    def get(self, request, id_codigo_cuenta):
        codigo = Cuenta.objects.get(codigo_cuenta=id_codigo_cuenta)
        form = self.form_class(instance=codigo)
        return render(request, self.template_name, {'form': form})

class ModificarCuenta(LoginRequiredMixin, View):
    login_url = '/'
    form_class = CuentaForm
    template_name = 'admin/modificar_cuenta.html'

    def get(self, request, id_codigo_cuenta):
        codigo = Cuenta.objects.get(codigo_cuenta=id_codigo_cuenta)
        form = self.form_class(instance=codigo)
        return render(request, self.template_name, {'form': form})

    def post(self, request, id_codigo_cuenta):
        codigo = Cuenta.objects.get(codigo_cuenta=id_codigo_cuenta)
        form = self.form_class(request.POST, request.FILES, instance=codigo)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'El Cuenta se modificó correctamente')

        else:
            messages.add_message(request, messages.ERROR, 'El Cuenta no se pudo modificar')

        listar = ListadoCuentas()
        return listar.get(request)

class BorrarCuenta(LoginRequiredMixin, View):
    login_url = '/'
    form_class = CuentaForm
    template_name = 'admin/borrar_cuenta.html'

    def get(self, request, id_codigo_cuenta):
        try:
            codigo = Cuenta.objects.get(codigo_cuenta=id_codigo_cuenta)
            form = self.form_class(instance=codigo)
            return render(request, self.template_name, {'form': form})

        except Cuenta.DoesNotExist:
            listar = ListadoCuentas()
            return listar.get(request)

    def post(self, request, id_codigo_cuenta):
        codigo = Cuenta.objects.get(codigo_cuenta=id_codigo_cuenta)
        codigo.delete()
        messages.add_message(request, messages.INFO, "La cuenta se borró correctamente")

        listar = ListadoCuentas()
        return listar.get(request)

class ListadoMovimientosReporte(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_movimientos_reporte.html'
    form_class = MovimientoForm

    def get(self, request):
        lista_movimientos = Movimiento.objects.all()
        return render(request, self.template_name, {'movimientos': lista_movimientos})

class ListadoMovimientos(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_movimientos.html'
    form_class = MovimientoForm

    def get(self, request):
        datos_usuario = Cliente.objects.get(usuid=request.user.pk)
        lista_movimientos = Movimiento.objects.filter(cliente=datos_usuario.pk)
        return render(request, self.template_name, {'movimientos': lista_movimientos, 'user': datos_usuario})

class ListadoMovimientosGeneral(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_movimientos_general.html'
    form_class = MovimientoForm

    def get(self, request):
        lista_movimientos = Movimiento.objects.all()
        return render(request, self.template_name, {'movimientos': lista_movimientos})

class ListadoMovimientosReporteByDate(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'admin/listar_movimientos_by_fecha.html'

    def get(self, request, id_cuen):
        return render(request, self.template_name)

    def post(self, request, id_cuen):
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        c = Cuenta.objects.get(pk=id_cuen)
        lista_movimientos = Movimiento.objects.filter(codigo_cuenta=c, fecha__gte=fecha_inicio, fecha__lte=fecha_fin)
        classmuestradatos = ListadoMovimientosReporteByFecha()
        return classmuestradatos.get(request, lista_movimientos, c)

class ListadoMovimientosReporteByFecha(LoginRequiredMixin, View):
    template_name = 'admin/listar_movimientos_por_fecha.html'
    def get(self, request, lista_movimientos, c):
        return render(request, self.template_name, {'movimientos': lista_movimientos, 'user': c.cliente})

class VisualizarMovimiento(LoginRequiredMixin, View):
    login_url = '/'
    form_class = MovimientoForm
    template_name = 'admin/visualizar_movimientos.html'

    def get(self, request, id_movimiento_visualizar):
        codigo = Movimiento.objects.get(id_movimiento=id_movimiento_visualizar)
        form = self.form_class(instance=codigo)
        return render(request, self.template_name, {'form': form})