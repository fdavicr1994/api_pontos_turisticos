# Generated by Django 2.2.1 on 2019-05-23 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pontoturistico_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='endereco',
        ),
    ]
