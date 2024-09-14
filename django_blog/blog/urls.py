from django.urls import path
from .views import register, user_login, user_logout, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
# blog/urls.py

# blog/urls.py

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),                     # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),    # View specific post details
    path('post/new/', PostCreateView.as_view(), name='post-create'),         # Create new post
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'), # Edit existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete specific post
]
