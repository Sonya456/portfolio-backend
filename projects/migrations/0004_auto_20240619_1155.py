# Generated by Django 3.2.25 on 2024-06-19 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='elements',
        ),
        migrations.AddField(
            model_name='project',
            name='default_image',
            field=models.ImageField(default=1, upload_to='project_images/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='projectelement',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='projects.project'),
        ),
    ]
