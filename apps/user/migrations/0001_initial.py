# Generated by Django 5.2 on 2025-04-12 22:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo_ciudad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_ciudad', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=50)),
                ('rol', models.CharField(choices=[('AMD', 'Administrador'), ('CLI', 'Cliente')], max_length=20)),
                ('codigo_ciudad', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='user.ciudad')),
                ('usuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('codigo_cuenta', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_cuenta', models.CharField(choices=[('COR', 'Corriente'), ('AHO', 'Ahorro')], max_length=25)),
                ('estado', models.CharField(choices=[('ACT', 'Activada'), ('DES', 'Desativada')], max_length=15)),
                ('saldo', models.FloatField(default=15000)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.cliente')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id_movimiento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(choices=[('RET', 'Retiro'), ('DEP', 'Deposito')], max_length=15)),
                ('saldo', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.cliente')),
                ('codigo_cuenta', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='user.cuenta')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
            },
        ),
    ]
