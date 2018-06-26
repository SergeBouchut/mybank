from rest_framework import serializers

from .models import Category, Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset=Category.objects.all().order_by('name')
    )
    class Meta:
        model = Transaction
        fields = ('id', 'date', 'description', 'amount', 'detail', 'category')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
