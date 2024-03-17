from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from shop.models import Supplier, Contact, Seller


class SupplierSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания Supplier"""
    contact = SlugRelatedField(slug_field="country", queryset=Contact.objects.all())

    class Meta:
        model = Supplier
        fields = '__all__'


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        read_only_fields = ('debt',)
