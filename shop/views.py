from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from shop.models import Supplier, Seller

from shop.serializers import SupplierSerializer, SellerUpdateSerializer


class SupplierCreateAPIView(CreateAPIView):
    """ Создание поставщика """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    def perform_create(self, serializer):
        new_supplier = serializer.save()
        new_supplier.user = self.request.user
        new_supplier.save()


class SupplierRetrieveAPIView(RetrieveAPIView):
    """ Просмотр одного поставщика """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierUpdateAPIView(UpdateAPIView):
    """ Редактирование поставщиков """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierDestroyAPIView(DestroyAPIView):
    """ Удаление поставщиков """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierListAPIView(ListAPIView):
    """ Список поставщиков """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contact__country']


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerUpdateSerializer
