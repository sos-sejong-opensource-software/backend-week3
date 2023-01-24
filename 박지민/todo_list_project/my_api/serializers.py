from django.core import serializers
from rest_framework import serializers
from .models import TodoModel

class TodoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"

