from django.shortcuts import render
from graphene_django.views import GraphQLView
from .schema import Query

def landing_page(request):
    return render(request, 'hospitals/landing_page.html', {'title': 'Hospital Management System'})

urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=graphene.Schema(query=Query))),
]
