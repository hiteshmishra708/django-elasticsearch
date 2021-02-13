from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from core import views
from django.contrib import admin
from core.views import get_product, search_product, search_supplier, search_category

router = routers.DefaultRouter()
router.register(r'supplier', views.SupplierViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^get_product/$', get_product),
    url(r'^search_product/$', search_product),
    url(r'^search_supplier/$', search_supplier),
    url(r'^search_category/$', search_category),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]