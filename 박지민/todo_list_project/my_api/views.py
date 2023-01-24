from my_api.models import TodoModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoPostSerializer

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.http import Http404

from django.shortcuts import get_object_or_404
def index(request):
    return HttpResponse("index view page")


@api_view(['GET'])
def get_api(request):
    todos = TodoModel.objects.all()
    serializer = TodoPostSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_api(request):
    if request.method == 'POST':
        serializer = TodoPostSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def sum_api(request, id):
    queryset = TodoModel.objects.all()
    serializer_class = GetSerializer
    postserializer_class=PostSerializr

    try:
        val = TodoModel.objects.get(pk = id)
    except TodoModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        todo = TodoPostSerializer(val)
        return Response(todo.data)

    elif request.method == 'PUT':
        serializer = TodoPostSerializer(val, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

