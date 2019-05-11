from django.db import models
from django.utils.translation import gettext as _


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(_('Name'), max_length=100)
    surname = models.CharField(_('Surname'), max_length=100)
    email = models.EmailField(_('Email'), max_length=254)
    telephone = models.CharField(_('Telephone'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=100, unique=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'Client Id: {self.client_id}'


class Payload(models.Model):
    loan_id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    term = models.IntegerField()
    rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'Payload Id: {self.loan_id}'
