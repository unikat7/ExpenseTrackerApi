from django.shortcuts import render
from .serializers import ExpenseSerializer
from rest_framework.views import APIView
from .models import Expense
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets

# Create your views here.


class ExpenseView(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




    

    
