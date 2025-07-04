from django.shortcuts import render
from .serializers import ExpenseSerializer
from rest_framework.views import APIView
from .models import Expense
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ExpenseView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




    

    
