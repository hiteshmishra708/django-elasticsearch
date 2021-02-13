from drf_elasticsearch_dsl.documents import ModelSerializerDocument
from elasticsearch_dsl import Date, Keyword, Text, String
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer


class CategorySerializerDocument(ModelSerializerDocument):
    name = String()
    desc = String()
    
    class Meta:
        index = 'category'
        serializer = CategorySerializer
        doc_type = 'django_rest.category'

class SupplierSerializerDocument(ModelSerializerDocument):
    name = String()
    desc = String()
    
    class Meta:
        index = 'supplier'
        serializer = SupplierSerializer
        doc_type = 'django_rest.supplier'

class ProductSerializerDocument(ModelSerializerDocument):
    name = String()
    desc = String()
    category_name = String()
    supplier_name = String()
    
    class Meta:
        index = 'product'
        serializer = ProductSerializer
        doc_type = 'django_rest.product'