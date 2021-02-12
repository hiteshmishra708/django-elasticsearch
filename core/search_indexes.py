from drf_elasticsearch_dsl.documents import ModelSerializerDocument
from elasticsearch_dsl import Date, Keyword, Text, String
from .serializers import CategorySerializer


class ContactSerializerDocument(ModelSerializerDocument):
    name = String()
    desc = Keyword()
    
    class Meta:
        index = 'product'
        serializer = CategorySerializer
        doc_type = 'django_rest.category'