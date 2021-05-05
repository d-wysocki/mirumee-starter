import graphene

from ..graphql.product.schema import ProductQueries


class Query(ProductQueries):
    pass

schema = graphene.Schema(query=Query)
