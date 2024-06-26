# Generated by Django 3.2.25 on 2024-06-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutelement',
            name='align',
            field=models.CharField(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')], default='center', max_length=10),
        ),
        migrations.AlterField(
            model_name='aboutelement',
            name='position',
            field=models.CharField(choices=[('left', 'Left'), ('right', 'Right'), ('top', 'Top'), ('bottom', 'Bottom')], default='center', max_length=10),
        ),
    ]
