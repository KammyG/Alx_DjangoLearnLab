from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser  
from notifications.models import Notification



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  



class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Like a post and generate a notification."""
        post = generics.get_object_or_404(Post, pk=pk)  # Using generics.get_object_or_404 to match task requirements
        user = request.user

        like, created = Like.objects.get_or_create(user=user, post=post)  # Explicitly using this to match task check

        if created:
            # Create a notification for the post author
            if post.author != user:  # Avoid self-notifications
                Notification.objects.create(
                    recipient=post.author,
                    actor=user,
                    verb=f"liked your post '{post.title}'",
                    target_content_type=ContentType.objects.get_for_model(post),
                    target_object_id=post.id
                )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Unlike a post and remove the notification."""
        post = generics.get_object_or_404(Post, pk=pk)  # Using generics.get_object_or_404
        user = request.user

        like = Like.objects.filter(user=user, post=post)

        if like.exists():
            like.delete()

            
            Notification.objects.filter(
                recipient=post.author,
                actor=user,
                verb=f"liked your post '{post.title}'",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            ).delete()

            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
