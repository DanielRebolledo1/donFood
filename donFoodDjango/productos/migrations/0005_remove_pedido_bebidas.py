# Generated by Django 4.0.4 on 2022-07-07 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_pedido_bebidas_pedido_comidas_delete_pedido_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='bebidas',
        ),
    ]
