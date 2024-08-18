from django.shortcuts import render
from django.views.generic import DetailView
from relationship_app.models import Book, Library  # Import both Book and Library models
from .models import Library
from django.views.generic.detail import DetailView
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
