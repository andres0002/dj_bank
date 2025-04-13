# django
from django import forms
from django.utils.translation import gettext_lazy as _
# third
# own
from apps.user.models import Cliente, Ciudad, Cuenta, Movimiento, ROL_CHOICES

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        labels = {
            'cedula': _(u'Número de Identificacion:'),
            'nombre': _(u'Nombre:'),
            'apellido': _(u'Apellido:'),
            'telefono': _(u'Telefono:'),
            'direccion': _(u'Direccion:'),
            'codigo_ciudad': _(u'Codigo Ciudad:'),
            'usuid': _(u'Username:'),
            'rol': _(u'Tipo de usuario')
        }

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = "__all__"
        labels = {
            'codigo_cuenta': _(u'Codigo Cuenta:'),
            'nombre_cuenta': _(u'Nombre Cuenta:'),
            'estado': _(u'Estado:'),
            'cliente': _(u'user:client:'),
            'saldo': _(u'Saldo')
        }

    def __init__(self, *args, **kwargs):
        super(CuentaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = "__all__"
        labels = {
            'id_movimiento': _(u'Codigo Movimiento:'),
            'cedula': _(u'Cedula:'),
            'codigo_cuenta': _(u'Codigo Cuenta:'),
            'fecha': _(u'Fecha Movimiento:'),
            'tipo': _(u'Tipo Movimientos:'),
            'saldo': _(u'Saldo Cuenta:')
        }

    def __init__(self, *args, **kwargs):
        super(MovimientoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AdicionarClienteForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    email = forms.EmailField(max_length=150, label='Email')
    password = forms.CharField(max_length=128, label='Contraseña', widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, label='Confirmar Contraseña', widget=forms.PasswordInput())
    cedula = forms.CharField(max_length=12, label='Cedula')
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=30, label='Apellido')
    telefono = forms.CharField(max_length=15, label='Telefono')
    direccion = forms.CharField(max_length=50, label='Direccion')
    nombre_ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), label='Ciudad')
    rol = forms.ChoiceField(choices=ROL_CHOICES, label='Tipo de Ususario', widget=forms.Select())