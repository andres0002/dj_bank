# django
from django.db import models
from django.contrib.auth.models import User
# third
# own

# Create your models here.

class Ciudad(models.Model):
    codigo_ciudad = models.CharField(max_length=10, primary_key=True)
    nombre_ciudad = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):        #__unicode__
        return self.nombre_ciudad

    class Meta:
        verbose_name_plural = "Ciudades"
        verbose_name = "Ciudad"

ROL_CHOICES = (
    ('AMD', u'Administrador'),
    ('CLI', u'Cliente')
)

class Cliente(models.Model):
    cedula = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    codigo_ciudad = models.ForeignKey(Ciudad, max_length=10, on_delete=models.CASCADE)
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

ESTADO = (
    ('ACT', u'Activada'),
    ('DES', u'Desativada')
)

NOMBRE_CUENTA = (
    ('COR', u'Corriente'),
    ('AHO', u'Ahorro')
)

class Cuenta(models.Model):
    codigo_cuenta = models.CharField(max_length=10, primary_key=True)
    nombre_cuenta = models.CharField(max_length=25, choices=NOMBRE_CUENTA)
    estado = models.CharField(max_length=15, choices=ESTADO)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo = models.FloatField(default=15000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_cuenta

    class Meta:
        verbose_name_plural = "Cuentas"
        verbose_name = "Cuenta"

TIPO_MOVIMIENTO = (
    ('RET', u'Retiro'),
    ('DEP', u'Deposito')
)

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigo_cuenta = models.ForeignKey(Cuenta, max_length=10, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=15, choices=TIPO_MOVIMIENTO)
    saldo = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name_plural = "Movimientos"
        verbose_name = "Movimiento"