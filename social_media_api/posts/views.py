from rest_framework import viewsets, permissions, generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser  # Explicitly importing CustomUser
from notifications.models import Notification

# ==========================
# Post Management Views
# ==========================

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set author to logged-in user

# ==========================
# Comment Management Views
# ==========================

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        
        # Create a notification for the post author
        if comment.post.author != self.request.user:  # Avoid self-notifications
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb=f"commented on your post '{comment.post.title}'"
            )

# ==========================
# User Feed View (Posts from Followed Users)
# ==========================

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Get posts from followed users, ordered by creation date."""
        user = self.request.user
        following_users = user.following.all()  # Get all users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

# ==========================
# Like & Unlike Post Views
# ==========================

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Like a post."""
        try:
            post = Post.objects.get(pk=pk)
            like, created = Like.objects.get_or_create(user=request.user, post=post)

            if created:
                # Create a notification for the post author
                if post.author != request.user:  # Avoid self-notifications
                    Notification.objects.create(
                        recipient=post.author,
                        actor=request.user,
                        verb=f"liked your post '{post.title}'"
                    )
                return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Unlike a post."""
        try:
            post = Post.objects.get(pk=pk)
            like = Like.objects.filter(user=request.user, post=post)

            if like.exists():
                like.delete()
                return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
