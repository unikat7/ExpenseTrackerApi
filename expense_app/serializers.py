from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()

    class Meta:
        model = Expense
        fields = ['title', 'description', 'amount', 'transaction_type', 'tax', 'tax_type', 'total_amount', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'total_amount']
