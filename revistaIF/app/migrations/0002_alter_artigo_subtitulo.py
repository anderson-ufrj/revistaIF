# Generated by Django 4.2.6 on 2023-11-07 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
