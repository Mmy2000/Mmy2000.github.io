# Generated by Django 4.2.5 on 2023-10-04 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_delete_imagesproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projectimages/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_image', to='projects.projects')),
            ],
        ),
    ]