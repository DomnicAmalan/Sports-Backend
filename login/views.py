from django.shortcuts import render, HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def login(request):
    return HttpResponse("Login")

@api_view(['POST'])
def signup(request):
    data = json.loads(request.body)
    print(data)
    return Response(status=400)