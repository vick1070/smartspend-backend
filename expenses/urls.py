from django.urls import path
from .views import (ExpenseListCreateView, ExpenseDetailView, CategoryListCreateView, CategoryDetailView)

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-list'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryListCreateView.as_view(), name='category-list'),
]
