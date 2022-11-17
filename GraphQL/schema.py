import graphene
from GraphQLapp.schema import Query as expq,Mutation


class Query(expq):
    pass

class Mutation(Mutation):
    pass

schema=graphene.Schema(query=Query,mutation=Mutation)
