# Generated by Django 4.2.4 on 2023-11-21 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0010_alter_ventaprod_ventas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventaprod',
            name='Ventas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventaprod_set', to='miAplicacion.ventas'),
        ),
    ]