from django.shortcuts import render
from rest_framework import generics
from .models import Mosque
from .serializers import MosqueListSerializer,MosqueDetailSerializer
# Create your views here.

class MosqueListAPIView(generics.ListAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueListSerializer

class MosqueDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Mosque.objects.all()
    serializer_class = MosqueDetailSerializer

class MosqueCreateAPIView(generics.CreateAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueDetailSerializer

class MosqueRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Mosque.objects.all()
    serializer_class = MosqueDetailSerializer

class MosqueDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Mosque.objects.all()