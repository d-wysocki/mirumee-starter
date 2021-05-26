import graphene

from .product.schema import ProductQueries, ProductMutations
from .checkout.schema import CheckoutMutations, CheckoutQueries


class Query(ProductQueries, CheckoutQueries):
    pass


class Mutations(ProductMutations, CheckoutMutations):
    pass


schema = graphene.Schema(query=Query,mutation=Mutations)
