import graphene
from graphene_django.types import DjangoObjectType
import json
import os
   

class Query(DjangoObjectType):
    name=graphene.String(value=graphene.String(default_value='warm'))
    age=graphene.String()

    def resolve_name(root,info,value):
        return value
    def resolve_age(root,info):
        return "25"

schema=graphene.Schema(query=Query)
print(schema)

# =============Graph Ql Query=============

# result=schema.execute(quer_graphql)
# print(json.dumps(result.data,indent=3))

# import graphene

# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")

# schema = graphene.Schema(query=Query)