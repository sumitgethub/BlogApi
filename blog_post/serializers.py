from rest_framework import serializers
from blog_post.models import BlogPost
from account.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 
                'is_active','email','created_at','updated_at','is_admin']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        # depth  = 1


    def to_representation(self, instance):
        response = super().to_representation(instance)

        # Adding author 
        response['author'] = UserSerializer(instance.author).data

        return response