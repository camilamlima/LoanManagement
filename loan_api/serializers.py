import decimal

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from decimal import Decimal
from datetime import datetime, timezone
from .models import Client, Loan, Payment


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, obj):
        return {
            "client_id": obj.client_id, 
        }


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"

    def to_representation(self, obj):
        a = str(obj.loan_id).zfill(15)
        return {
            "loan_id": f'{a[0:3]}-{a[3:7]}-{a[7:11]}-{a[11:]}',
            "installment": obj.instalment
        }

    def validate(self, data):
        loan = Loan.objects.filter(client_id=data['client_id'])
        has_payment = False
        times_missed = 0
        for i in loan:
            try:
                payment = Payment.objects.get(loan_id=i.loan_id)
                has_payment = True
                made_or_not = payment.payment
                if made_or_not == 'missed':
                    times_missed += 1
            except ObjectDoesNotExist:
                pass
        if times_missed == 0 and has_payment:
            data['rate'] -= decimal.Decimal('0.02')
            return data
        elif times_missed < 3 and has_payment:
            data['rate'] += decimal.Decimal('0.04')
            return data
        elif times_missed >= 3:
            raise serializers.ValidationError("Cliente não pagou 3 ou mais faturas.")
        elif not has_payment:
            return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def to_representation(self, obj):
        return {}


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"

    def to_representation(self, obj):
        return {
            "balance": obj.balance
        }
