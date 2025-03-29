from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
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
        post = generics.get_object_or_404(Post, pk=pk)  
        user = request.user

        
        like, created = Like.objects.get_or_create(user=request.user, post=post) 

        if created:
            if post.author != request.user:  
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb=f"liked your post '{post.title}'"
                )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Unlike a post."""
        post = generics.get_object_or_404(Post, pk=pk)  
        user = request.user

        like = Like.objects.filter(user=request.user, post=post)

        if like.exists():
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
