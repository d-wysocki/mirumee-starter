import graphene

from .types import UserType
from ...account.models import User


class UserCreateInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    first_name = graphene.String(required=False)
    last_name = graphene.String(required=False)


class UserCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    def mutate(cls, root, _info, input):
        user = User.objects.create_user(**input)
        return UserCreate(user=user)


class StaffCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    def mutate(cls, root, _info, input):
        staff = User.objects.create_user(**input, is_staff=True)
        return StaffCreate(user=staff)