from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
Post.objects.filter(author__in=following_users).order_by", "following.all()
generics.get_object_or_404(Post, pk=pk)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
from django_filters.rest_framework import FilterSet

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['exact', 'icontains'],
            'content': ['icontains'],
        }

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = PostFilter
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get posts from users that the current user follows
        following_ids = self.request.user.following.values_list('id', flat=True)
        return Post.objects.filter(author__id__in=following_ids).order_by('-created_at')
from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )
            return Response({"message": "Post liked."})
        return Response({"message": "You already liked this post."})

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Post unliked."})
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post."})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post  # Import your Post model

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()  # Assuming you have a following relationship
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        # Serialize the posts as needed
        serialized_posts = PostSerializer(posts, many=True)  # Adjust based on your serializer
        return Response(serialized_posts.data)
