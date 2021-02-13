from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import SupplierSerializer, CategorySerializer, ProductSerializer 
from .models import Supplier, Category, Product
from django.http import JsonResponse
from .documents import ProductDocument, SupplierDocument, CategoryDocument


class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows supplier to be viewed or edited.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = Product

def get_product(request):
    name = request.GET.get('name')

    if name is not None:
        return JsonResponse({
            'code': 200,
            'message': 'success',
            'data': [obj.get_obj() for obj in Product.objects.filter(name__contains=name)]
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': 'Search query invalid'
        })

def search_product(request):
    name = request.GET.get('query')

    s = ProductDocument.search().query("match", name=name)
    qs = s.to_queryset()

    if name is not None:
        return JsonResponse({
            'code': 200,
            'message': 'success',
            'data': [obj.get_obj() for obj in qs]
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': 'Search query invalid'
        })

def search_supplier(request):
    name = request.GET.get('query')

    s = ProductDocument.search().query("match", name=name)
    qs = s.to_queryset()

    if name is not None:
        return JsonResponse({
            'code': 200,
            'message': 'success',
            'data': [obj.get_obj() for obj in qs]
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': 'Search query invalid'
        })

def search_category(request):
    name = request.GET.get('query')

    s = ProductDocument.search().query("match", name=name)
    qs = s.to_queryset()

    if name is not None:
        return JsonResponse({
            'code': 200,
            'message': 'success',
            'data': [obj.get_obj() for obj in qs]
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': 'Search query invalid'
        })