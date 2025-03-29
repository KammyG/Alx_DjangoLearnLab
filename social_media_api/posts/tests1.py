from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post

User = get_user_model()

class PostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        data = {"title": "Test Post", "content": "This is a test."}
        response = self.client.post("/posts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "Test Post")
