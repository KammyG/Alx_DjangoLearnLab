from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class FollowTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
        self.client.login(username="user1", password="password")

    def test_follow_user(self):
        response = self.client.post(f"/api/accounts/follow/{self.user2.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user1.following.filter(id=self.user2.id).exists())

    def test_unfollow_user(self):
        self.user1.follow(self.user2)
        response = self.client.post(f"/api/accounts/unfollow/{self.user2.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user1.following.filter(id=self.user2.id).exists())
