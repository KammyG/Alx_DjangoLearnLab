from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

charfield_instance = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)  
        Token.objects.create(user=user)
        return user

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'following']
        read_only_fields = ['id', 'username']

    def update(self, instance, validated_data):
        request = self.context.get("request")
        target_user = validated_data.get("following")

        if target_user and request:
            if request.method == "POST":
                instance.follow(target_user)
            elif request.method == "DELETE":
                instance.unfollow(target_user)
            instance.save()
        
        return instance

