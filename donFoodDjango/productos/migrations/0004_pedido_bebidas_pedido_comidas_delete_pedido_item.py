# Generated by Django 4.0.4 on 2022-07-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_pedido_pedido_item_delete_orden'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='bebidas',
            field=models.ManyToManyField(to='productos.bebida'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='comidas',
            field=models.ManyToManyField(to='productos.comida'),
        ),
        migrations.DeleteModel(
            name='Pedido_item',
        ),
    ]
