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



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        
        
        if comment.post.author != self.request.user:  
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb=f"commented on your post '{comment.post.title}'",
                target_content_type=ContentType.objects.get_for_model(comment.post),
                target_object_id=comment.post.id
            )



class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Get posts from followed users, ordered by creation date."""
        user = self.request.user
        following_users = user.following.all()  # Get all users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')



class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Like a post and generate a notification."""
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        like, created = Like.objects.get_or_create(user=user, post=post)

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
        post = get_object_or_404(Post, pk=pk)
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
