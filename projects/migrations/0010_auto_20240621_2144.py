# Generated by Django 3.2.25 on 2024-06-21 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20240621_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutelement',
            name='align',
        ),
        migrations.RemoveField(
            model_name='aboutelement',
            name='position',
        ),
    ]