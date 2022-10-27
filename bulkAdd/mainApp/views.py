from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

class MusicianViewSet(viewsets.ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

class BulkMusicianAdd(APIView):
    def post(self, request):
        [Musician.objects.create(**musician) for musician in request.data]
        return Response({"msg":"Inserted Successfully"})