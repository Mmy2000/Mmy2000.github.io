# Generated by Django 4.2.5 on 2023-09-28 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0004_remove_about_join_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('university', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(max_length=100000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]