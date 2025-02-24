from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('Username', 'FirstName', 'LastName', 'Email', 'Mobile')