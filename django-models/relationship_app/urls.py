<<<<<<< HEAD
from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
=======
from django.urls import path
from relationship_app import views
from .views import list_books
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
>>>>>>> 063c4d52038628360ec3ace8ec01fc697f20f7d8
