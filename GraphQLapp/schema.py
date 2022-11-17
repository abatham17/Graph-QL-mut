import graphene
from graphene_django.types import DjangoObjectType
from .models import NYC_data
from graphene_django.forms.mutation import DjangoFormMutation
import requests
import json

class expdata(DjangoObjectType):
    class Meta:
        model=NYC_data

class Query(graphene.ObjectType):
    all_data=graphene.List(expdata,ide=graphene.Int())

    def resolve_all_data(root,info,ide):
        return NYC_data.objects.filter(id=ide)


class dataMutation(graphene.Mutation):
    class Arguments:
        zip_code=graphene.String(required=True)
        street=graphene.String(required=True)
    data=graphene.Field(expdata)

    @classmethod
    def mutate(cls,root,info,zip_code,street):
        data=NYC_data.objects.get(zip_code=zip_code)
        data.street_name=street
        data.save()
        return dataMutation(zip_code=zip_code)

class Mutation(graphene.ObjectType):
    update_data=dataMutation.Field()
