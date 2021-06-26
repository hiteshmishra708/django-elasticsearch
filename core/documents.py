from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from core.models import Product, Supplier, Category

@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(properties={
        'name': fields.TextField(),
        'desc': fields.TextField()
    })

    supplier = fields.ObjectField(properties={
        'name': fields.TextField()
    })

    class Index:
        name = 'products'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    
    class Django:
        model = Product

        fields = [
            'name',
            'desc'
        ]

        related_models = [Category, Supplier]

        def get_queryset(self):
            return super(ProductDocument, self).get_queryset().select_related(
            'category', 'supplier')

        def get_instances_from_related(self, related_instance):
            if isinstance(related_instance, Category):
                return related_instance.category_set.all()

            if isinstance(related_instance, Supplier):
                return related_instance.supplier_set.all()

@registry.register_document
class SupplierDocument(Document):
    class Index:
        name = 'supplier'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Supplier

        fields = [
            'name',
        ]

@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'category'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Category

        fields = [
            'name',
            'desc',
        ]