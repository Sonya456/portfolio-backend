# Generated by Django 3.2.25 on 2024-06-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20240619_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='default_image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/'),
        ),
    ]
