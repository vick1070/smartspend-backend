#\89from django.shortcuts import render/*
from rest_framework import generics
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

# Create your views here.

# --Expense Views--

#List all expense or create a new one
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
#Retrieve, update, or delete a sinle expense
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
# --Category View--

#List all categories or create new one
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
#Retrive, update, or delete a single category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer