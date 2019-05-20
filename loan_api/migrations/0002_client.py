# Generated by Django 2.2.1 on 2019-05-16 23:47

from django.db import migrations, models
from ..validators import validate_cpf, validate_phone


class Migration(migrations.Migration):

    dependencies = [
        ('loan_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telephone', models.CharField(max_length=11, validators=[validate_phone], verbose_name='Telephone')),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[validate_cpf], verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
