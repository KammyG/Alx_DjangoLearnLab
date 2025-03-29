from rest_framework import generics, permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import CustomUser  # Explicitly importing CustomUser
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Using CustomUser explicitly
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # Using CustomUser explicitly
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Follow a user."""
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.follow(user_to_follow)
        return Response({"message": "You are now following this user."}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # Using CustomUser explicitly
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Unfollow a user."""
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.unfollow(user_to_unfollow)
        return Response({"message": "You have unfollowed this user."}, status=status.HTTP_200_OK)
