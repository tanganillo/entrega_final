# Generated by Django 5.2.4 on 2025-07-22 14:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_noticia_delete_pagina'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noticia',
            name='etiquetas',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='noticia',
            name='genero',
            field=models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('trap', 'Trap'), ('reggaeton', 'Reggaetón'), ('electronica', 'Electrónica')], default='General', max_length=100),
        ),
    ]
