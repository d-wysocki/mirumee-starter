import graphene

from .types import ProductType
from ...product.models import Product


class ProductQueries(graphene.ObjectType):
    product = graphene.Field(
        ProductType, id=graphene.Argument(graphene.ID, description="ID of product.")
    )

    def resolve_product(self, _info, id):
        product = Product.objects.filter(id=id).first()
        return product
