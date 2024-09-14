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

from django.urls import path
from .views import PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # URL pattern for creating a new comment associated with a post
    path('post/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    
    # URL pattern for updating an existing comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    
    # URL pattern for deleting an existing comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
