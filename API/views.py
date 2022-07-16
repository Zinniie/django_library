from django.shortcuts import render



from rest_framework import generics


from API.models import Book
from .serializers import BookSerializer

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookApiCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookApiDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookApiUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookApiDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





    