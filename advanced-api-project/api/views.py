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
# views.py
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    
    # Define filter fields
    filterset_fields = {
        'title': ['exact', 'icontains'],
        'author': ['exact', 'icontains'],
        'published_date': ['exact', 'year__gt', 'year__lt'],
    }
    
    # Define search fields
    search_fields = ['title', 'author']
    
    # Define ordering fields
    ordering_fields = ['title', 'published_date']
    ordering = ['title']  # Default ordering

