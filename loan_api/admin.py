from django.contrib import admin
from .models import Payload, Client


class PayloadAdmin(admin.ModelAdmin):
    list_display = [
        'loan_id',
        'amount',
        'term',
        'rate',
        'date'
    ]

class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'client_id',
        'name',
        'surname',
        'email',
        'telephone',
        'cpf',
    ]


admin.site.register(Payload, PayloadAdmin)
admin.site.register(Client, ClientAdmin)