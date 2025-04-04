from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts
)

urlpatterns = [
    # Authentication URLs
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),

    # Blog Post URLs
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comment URLs (Updated Structure)
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),  # Create comment
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),  # Edit comment
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),  # Delete comment

        # Search URL
    path("search/", search_posts, name="search-posts"),
]
