# Generated by Django 4.0.2 on 2023-12-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.CharField(max_length=100),
        ),
    ]
