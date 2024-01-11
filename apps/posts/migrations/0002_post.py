# Generated by Django 5.0.1 on 2024-01-11 04:47

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, default='static/posts_default.png', null=True, upload_to='media')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(default='Sin categoría', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.categoria')),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
    ]
