# Generated by Django 4.2.4 on 2023-09-27 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0003_alter_cliente_direccion_alter_cliente_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='Producto',
        ),
    ]
