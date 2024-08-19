from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from users.models import Problems, Comments, Advisers
from .serializers import CategorySerializer
from .serializers import ServicesSerializer, FeaturesSerializer, BlogSerializer, BlogTypeSerializer, AdvisersSerializer
from .serializers import ProblemsSerializer, UserSerializer, CategorySerializer, CommentsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.db.transaction import atomic
from servic.models import Category, Services, Features, Blog, BlogType
from django.utils import timezone
from datetime import datetime


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', '^name']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def open_page(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category, many=False)
        created = category.create_time
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category, many=False)
        updated = category.update_time
        return Response(data={'updated': updated}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        category = self.get_object()
        with atomic():
            category.views = category.views + 1
            category.save()
            return Response(status.HTTP_204_NO_CONTENT)


class FeaturesViewSet(ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        city = self.get_object()
        serializer = FeaturesSerializer(city, many=False)
        updated = city.last_update_time
        return Response(data={'updated': updated}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        city = self.get_queryset()
        city = city.order_by('name')
        serializer = FeaturesSerializer(city, many=True)
        return Response(data=serializer.data)


class BlogTypeViewSet(ModelViewSet):
    queryset = BlogType.objects.all()
    serializer_class = BlogTypeSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for blog in self.get_queryset():
                day = (today - blog.create_time.date()).days
                results.append({
                    'id': blog.id,
                    'update_time': blog.create_time,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        blog = self.get_queryset()
        blog = blog.order_by('name')
        serializer = BlogTypeSerializer(blog, many=True)
        return Response(data=serializer.data)


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for blog in self.get_queryset():
                day = (today - blog.last_update_time.date()).days
                results.append({
                    'id': blog.id,
                    'update_time': blog.last_update_time,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        blog = self.get_queryset()
        blog = blog.order_by('name')
        serializer = BlogSerializer(blog, many=True)
        return Response(data=serializer.data)


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'short_name',
                     'description']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        services = self.get_queryset()
        services = services.order_by('short_name')
        serializer = ServicesSerializer(services, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def open_page(self, request, *args, **kwargs):
        services = self.get_object()
        serializer = ServicesSerializer(services, many=False)
        created = services.build_date
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        services = self.get_queryset()
        services = services.order_by('price')
        serializer = ServicesSerializer(services, many=True)
        return Response(data=serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'user', 'comment', 'comment_title']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def open_comment(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = CommentsSerializer(comment, many=False)
        created = comment.created
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        comment = self.get_queryset()
        comment = comment.order_by('comment_title')
        serializer = ServicesSerializer(comment, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for blog in self.get_queryset():
                day = (today - blog.created.date()).days
                results.append({
                    'id': blog.id,
                    'update_time': blog.created,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)


class ProblemViewSet(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'firstname', 'email', 'problem_name', 'problem_description']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def write_problem_time(self, request, *args, **kwargs):
        problem = self.get_object()
        serializer = ProblemsSerializer(problem, many=False)
        created = problem.created_at
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        problem = self.get_queryset()
        problem = problem.order_by('created_at')
        serializer = ProblemsSerializer(problem, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for blog in self.get_queryset():
                day = (today - blog.created_at.date()).days
                results.append({
                    'id': blog.id,
                    'update_time': blog.created_at,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)


class AdvisersViewSet(ModelViewSet):
    queryset = Advisers.objects.all()
    serializer_class = AdvisersSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['firstname', 'lastname', 'email', 'username', 'phone',
                     'work_price', 'views', 'profession']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def sum(self, request, *args, **kwargs):
        for obj in self.queryset:
            s = obj.work_price * obj.count_sold
        context ={
            'work_price': obj.work_price,
            'sum': s
        }
        return Response(data=context, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        advisers = self.get_queryset()
        advisers = advisers.order_by('work_price')
        serializer = AdvisersSerializer(advisers, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        advisers = self.get_object()
        with atomic():
            advisers.views = advisers.views + 1
            advisers.save()
            return Response(status.HTTP_204_NO_CONTENT)
