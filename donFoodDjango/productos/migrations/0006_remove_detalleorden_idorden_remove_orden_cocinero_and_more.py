# Generated by Django 4.0.4 on 2022-05-23 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_r_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleorden',
            name='idOrden',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='cocinero',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='idComida',
        ),
        migrations.DeleteModel(
            name='R_usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Cocinero',
        ),
        migrations.DeleteModel(
            name='Comida',
        ),
        migrations.DeleteModel(
            name='DetalleOrden',
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
    ]