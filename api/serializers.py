from rest_framework import serializers
from servic.models import Category, Services, BlogType, Blog, Features
from users.models import Comments, Problems, Advisers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['id', 'name', 'description']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'views', 'image']


class BlogTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = ['id', 'name']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'image', 'blog_type']


class AdvisersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisers
        fields = ['id', 'firstname', 'lastname', 'email', 'username', 'password', 'phone', 'work_price', 'work_time',
                  'experience', 'count_sold', 'views', 'photo']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'comment_title', 'comment']


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = ['id', 'firstname', 'email', 'problem_name', 'problem_description']


class ServicesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    features = FeaturesSerializer(read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'short_name', 'description', 'image']




