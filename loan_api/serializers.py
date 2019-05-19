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
        return {
            "loan_id": str(obj.loan_id), 
            "installment": obj.instalment
            
        }


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def to_representation(self, obj):
        return {}
