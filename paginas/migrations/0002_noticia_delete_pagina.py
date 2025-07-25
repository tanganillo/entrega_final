# Generated by Django 5.2.4 on 2025-07-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='noticias/')),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Pagina',
        ),
    ]
