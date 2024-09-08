# views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
IsAuthenticated

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
CreateView
UpdateView 
DeleteView
