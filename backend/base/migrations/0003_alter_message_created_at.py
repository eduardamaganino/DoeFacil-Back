# Generated by Django 4.0.2 on 2023-12-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
