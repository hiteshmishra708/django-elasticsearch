from rest_framework import serializers
from .models import Supplier, Category, Product

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='cat.name')
    supplier_name = serializers.CharField(source='supplied_by.name')
    search_auto = serializers.CharField(source='name' + ' ' + 'cat.name' + 'supplied_by.name')

    class Meta:
        model = Product
        # fields = ('__all__')
        # fields = ('id', 'name', 'desc',)
        fields = ('id', 'name', 'desc', 'category_name', 'supplier_name', 'search_auto')