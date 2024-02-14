

import graphene
from graphene_django.types import DjangoObjectType
from .models import Hospital


class HospitalType(DjangoObjectType):
    class Meta:
        model = Hospital

class Query(graphene.ObjectType):
    all_hospitals = graphene.List(HospitalType)

    def resolve_all_hospitals(self, info):
        return Hospital.objects.all()
