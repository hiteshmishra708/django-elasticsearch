from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Supplier, Category, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='cat.name')
    supplier_name = serializers.CharField(source='supplied_by.name')

    class Meta:
        model = Product
        fields = ('name', 'desc', 'category_name', 'supplier_name')