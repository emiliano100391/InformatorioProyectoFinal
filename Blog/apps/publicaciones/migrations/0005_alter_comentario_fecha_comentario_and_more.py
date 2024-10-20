# Generated by Django 5.1.1 on 2024-10-08 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_alter_comentario_fecha_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 8, 0, 32, 40, 613612, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_creacion_public',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 8, 0, 32, 40, 612612, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen_public',
            field=models.ImageField(blank=True, help_text='selecciona una imagen para la publicación', null=True, upload_to='media/img'),
        ),
    ]
