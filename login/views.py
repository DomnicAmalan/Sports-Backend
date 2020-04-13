from rest_framework import viewsets, status
from rest_framework.response import Response
from . import models
from . import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.views.generic.base import View


@method_decorator(csrf_exempt, name='dispatch')
class UserViewset(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserViewset, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(serializers.UserSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        print("get", args)
        user = get_object_or_404(models.User, pk=kwargs['Username'])
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = get_object_or_404(models.User, pk=kwargs['Username'])
        serializer = serializers.UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(serializers.UserSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        question = get_object_or_404(models.User, pk=kwargs['Username'])
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)
       
    