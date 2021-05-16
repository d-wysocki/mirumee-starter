from graphene_django import DjangoObjectType

from ...product.models import Product, ProductVariant


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'


class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVariant
        fields = '__all__'
