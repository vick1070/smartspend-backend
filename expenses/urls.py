from django.urls import path
from .views import (ExpenseListCreateView, ExpenseDetailView, CategoryListCreateView, CategoryDetailView, RegisterView)

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]
