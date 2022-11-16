# Generated by Django 3.1.5 on 2021-10-12 13:32

from django.db import migrations, models
import validation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
                ('cpf_cnpj', models.CharField(max_length=11, verbose_name='CPF/CNPJ')),
                ('phone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('code', models.CharField(max_length=128, verbose_name='Código de Validação')),
                ('expires_date', models.DateTimeField(default=validation.models.validation_expires_date, verbose_name='Data de Validade')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Validação de Cadastro',
                'verbose_name_plural': 'Validações de Cadastros',
            },
        ),
    ]
