# Generated by Django 5.0.1 on 2024-01-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user_email',
            field=models.CharField(default='athi@gmail.com', max_length=255),
            preserve_default=False,
        ),
    ]
