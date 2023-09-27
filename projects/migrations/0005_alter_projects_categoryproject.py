# Generated by Django 4.2.5 on 2023-09-27 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projects_categoryproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='categoryproject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_category', to='projects.categoryproject', verbose_name='categoryproject'),
        ),
    ]
