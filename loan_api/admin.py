from django.contrib import admin
from .models import Payload


class PayloadAdmin(admin.ModelAdmin):
    list_display = [
        'loan_id',
        'amount',
        'term',
        'rate',
        'date'
    ]


admin.site.register(Payload, PayloadAdmin)
