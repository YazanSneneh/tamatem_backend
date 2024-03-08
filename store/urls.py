from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import ItemViewSet, ItemImageViewSet

router = DefaultRouter()
router.register('items', ItemViewSet, basename='items')

item_nested_router = NestedDefaultRouter(router, 'items', lookup='item')
item_nested_router.register('images', ItemImageViewSet, basename='item-images')

urlpatterns = [
    path('', include(router.get_urls())),
    path(r'', include(item_nested_router.urls)),
]