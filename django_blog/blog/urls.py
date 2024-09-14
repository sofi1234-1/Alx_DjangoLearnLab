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

# blog/urls.py

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),                     # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),    # View specific post details
    path('post/new/', PostCreateView.as_view(), name='post-create'),         # Create new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete specific post
]
# blog/urls.py

# blog/urls.py

# blog/urls.py

from django.urls import path
from .views import PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # URL pattern for displaying a specific post along with its comments
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # URL pattern for creating a new comment associated with a specific post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    
    # URL pattern for editing an existing comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    
    # URL pattern for deleting an existing comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<str:tag_name>/', views.TagView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
]
