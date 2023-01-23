from rest_framework.response import Response
from rest_framework import status, generics
from .models import NoteModel
from .serializers import NoteSerializer,PostSerializr,GetSerializer


class Show(generics.GenericAPIView):
    serializer_class = NoteSerializer
    postserializer_class=PostSerializr
    queryset = NoteModel.objects.all()

    def get(self, request):
        notes = NoteModel.objects.all()
        
        serializer = self.serializer_class(notes, many=True)
        return Response(
             serializer.data
        )

    def post(self, request):
        serializer = self.postserializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowDetail(generics.GenericAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = GetSerializer
    postserializer_class=PostSerializr
    def get_note(self, pk):
        try:
            return NoteModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        note = self.get_note(pk)
        serializer = self.serializer_class(note)
        return Response(serializer.data)

    #update
    def patch(self, request, pk):
        
        note = self.get_note(pk)
        serializer = self.postserializer_class(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_note(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)