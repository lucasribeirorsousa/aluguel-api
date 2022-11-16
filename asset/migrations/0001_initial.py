# Generated by Django 3.1.5 on 2021-10-12 13:32

import asset.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.PositiveSmallIntegerField(choices=[(1, 'image'), (2, 'banner'), (3, 'other')], default=1, verbose_name='Tipo de Arquivo')),
                ('file_high', models.FileField(upload_to=asset.models.upload_directory_path, verbose_name='Arquivo (high)')),
                ('file_medium', models.FileField(null=True, upload_to=asset.models.upload_directory_path, verbose_name='Arquivo (medium)')),
                ('file_low', models.FileField(null=True, upload_to=asset.models.upload_directory_path, verbose_name='Arquivo (low)')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
            ],
            options={
                'verbose_name': 'Arquivo',
                'verbose_name_plural': 'Arquivos',
            },
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('location', models.CharField(choices=[('principal', 'principal_spot')], max_length=20, unique=True, verbose_name='Localização do Spot')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hyperlink', models.CharField(max_length=255, verbose_name='Hyperlink')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('expires', models.DateTimeField(verbose_name='Data e Hora de expiração')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.asset')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.spot')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
    ]
