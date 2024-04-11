from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view # Required to use the Response


@api_view(['GET'])
def getRoutes(requests):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)