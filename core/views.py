from rest_framework import viewsets
from core.serializers import SupplierSerializer, CategorySerializer, ProductSerializer
from core.models import Supplier, Category, Product, Response
from django.http import JsonResponse
from core.documents import ProductDocument
from django.views.decorators.csrf import csrf_exempt
from elasticsearch_dsl.query import MultiMatch

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
    serializer_class = ProductSerializer

@csrf_exempt
def get_product(request):
    name = request.GET.get('name')

    if name is not None:
        return Response([obj.get_obj() for obj in Product.objects.filter(name__contains=name)]).get_obj()
    else:
        return JsonResponse({
            'code': 400,
            'message': 'Search query invalid'
        })

@csrf_exempt
def search_product(request):
    query = request.GET.get('query')

    # s = ProductDocument.search().query("match", name=query)
    # qs = s.to_queryset()

    p = MultiMatch(query=query, fields=['query', 'desc'], fuzziness='AUTO')
    s = ProductDocument.search().query(p)
    qs = s.to_queryset()
    # response = s.execute()

    if query is not None:
        return Response([obj.get_obj() for obj in qs]).get_obj()
    else:
        return Response(400, 'Search query invalid')

@csrf_exempt
def search_supplier(request):
    query = request.GET.get('query')

    s = ProductDocument.search().query("match", name=query)
    qs = s.to_queryset()

    # from elasticsearch_dsl.query import Q
    # p = Q("multi_match", query=query, fields=['name','category__name', 'supplier__name'],
    #                 type='phrase_prefix')
    # s = ProductDocument.search().query(p)
    # qs = s.to_queryset()
    # result = s.execute()

    if query is not None:
        return Response([obj.get_obj() for obj in qs]).get_obj()
    else:
        return Response(400, 'Search query invalid')
@csrf_exempt
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