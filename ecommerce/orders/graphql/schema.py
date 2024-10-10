import graphene
from graphene_django import DjangoObjectType
from .models import Order

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)

    def resolve_orders(self, info):
        return Order.objects.all()

class CreateOrder(graphene.Mutation):
    class Arguments:
        product_id = graphene.Int()
        quantity = graphene.Int()

    success = graphene.Boolean()

    def mutate(self, info, product_id, quantity):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Authentication required')

        product = Product.objects.get(id=product_id)
        total_price = product.price * quantity

        order = Order.objects.create(user=user, product=product, quantity=quantity, total_price=total_price, status='PENDING')
        return CreateOrder(success=True)

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
