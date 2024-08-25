
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Library
from django.contrib.auth import login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')  # Redirect to a page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'relationship_app/login.html')

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('list_books')  # Redirect to a page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

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
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # Your view logic here
    # This view will only be accessible to users with the 'Admin' role

@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    # Your view logic here
    # This view will only be accessible to users with the 'Librarian' role

@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    # Your view logic here
    # This view will only be accessible to users with the 'Member' role
from django.contrib.auth.decorators import permission_required
relationship_app.can_add_book
relationship_app.can_change_book", "relationship_app.can_delete_book
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    # Your 'Admin' view logic here
    return render(request, 'admin_template.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    # Your 'Librarian' view logic here
    return render(request, 'librarian_template.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    # Your 'Member' view logic here
    return render(request, 'member_template.html')
# views.py

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'role_based_views/adminview.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'role_based_views/librarianview.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'role_based_views/memberview.html')
relationship_app/member_view.html
relationship_app/librarian_view.html
relationship_app/admin_view.html
