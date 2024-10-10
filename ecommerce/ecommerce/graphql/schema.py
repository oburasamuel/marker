import graphene
import products.graphql.schema
import users.graphql.schema
import orders.graphql.schema

class Query(products.graphql.schema.Query, users.graphql.schema.Query, orders.graphql.schema.Query, graphene.ObjectType):
    pass

class Mutation(orders.graphql.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
