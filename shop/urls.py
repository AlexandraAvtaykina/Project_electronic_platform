from django.urls import path
from rest_framework.routers import DefaultRouter

from shop.apps import ShopConfig
from shop.views import SupplierCreateAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, SupplierDestroyAPIView, \
    SupplierListAPIView, SellerViewSet

app_name = ShopConfig.name

router = DefaultRouter()
router.register(r'seller', SellerViewSet, basename='seller')

urlpatterns = [
    path('create/', SupplierCreateAPIView.as_view(),
         name='create_supplier'),

    path('retrieve/<int:pk>/', SupplierRetrieveAPIView.as_view(),
         name='retrieve_supplier'),

    path('update/<int:pk>/', SupplierUpdateAPIView.as_view(),
         name='update_supplier'),

    path('destroy/<int:pk>/', SupplierDestroyAPIView.as_view(),
         name='destroy_supplier'),

    path('list/', SupplierListAPIView.as_view(),
         name='list_supplier'),
] + router.urls
