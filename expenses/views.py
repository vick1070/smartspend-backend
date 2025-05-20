#\89from django.shortcuts import render/*
from rest_framework import generics, permissions
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

# Create your views here.

# --Expense Views--

#List all expense or create a new one
class ExpenseListCreateView(generics.ListCreateAPIView):
    #queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        print(">>> request.user:", self.request.user)
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
#Retrieve, update, or delete a sinle expense
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        print(">>> request.user:", self.request.user)
        return Expense.objects.filter(user=self.request.user)
         
# --Category View--

#List all categories or create new one
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
#Retrive, update, or delete a single category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    