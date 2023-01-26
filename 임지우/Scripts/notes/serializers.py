from rest_framework import serializers
from .models import NoteModel

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['title','id']

class PostSerializr(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['title','description','createdAt','updatedAt']

        

class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['title']
