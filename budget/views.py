from django.shortcuts import render

from rest_framework import viewsets

from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer


DEFAULT_START, DEFAULT_END = 0, 50


def base(request):
    return render(request, 'budget/base.html')


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-date')[:20]
    serializer_class = TransactionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
