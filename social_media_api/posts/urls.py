from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import PostListCreateView
from .views import UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', PostListCreateView.as_view(), name='post-list-create'),
     path('feed/', UserFeedView.as_view(), name='user-feed'),
]
