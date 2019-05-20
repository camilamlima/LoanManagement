import decimal

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from decimal import Decimal
from datetime import datetime, timezone
from .models import Client, Loan, Payment


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def to_representation(self, obj):
        return {"client_id": obj.client_id}


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"

    def to_representation(self, obj):
        a = str(obj.loan_id).zfill(15)
        return {
            "loan_id": f"{a[0:3]}-{a[3:7]}-{a[7:11]}-{a[11:]}",
            "installment": obj.instalment,
        }

    def validate(self, data):
        loans = Loan.objects.filter(client_id=data["client_id"])

        if loans:
            times_missed = 0
            balance_all = 0

            for loan in loans:
                balance_all += loan.balance
                payment = Payment.objects.filter(loan_id=loan.loan_id, payment="missed")
                times_missed += len(payment)

            if balance_all != 0 or times_missed > 3:
                # Business rule #3
                raise serializers.ValidationError("Deny")

            if times_missed == 0:
                # Business rule #1
                data["rate"] -= decimal.Decimal("0.02")
                return data
            elif times_missed <= 3:
                # Business rule #2
                data["rate"] += decimal.Decimal("0.04")
                return data

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
        return {"balance": obj.balance}
