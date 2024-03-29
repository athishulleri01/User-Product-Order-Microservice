# Generated by Django 5.0.1 on 2024-01-31 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.user'),
        ),
    ]
