# Generated by Django 2.2.1 on 2019-05-03 02:22

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Amount')),
                ('term', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Term')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Rate')),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
        ),
    ]
