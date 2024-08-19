from django.contrib import admin
from django.urls import path, include
from .views import (
    AdvisersViewSet, BlogViewSet, BlogTypeViewSet, CategoryViewSet,
    CommentViewSet, ProblemViewSet, FeaturesViewSet, ServicesViewSet
)
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view setup
schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        description="Application demo makan",
        default_version="v1",
        terms_of_service='http://demo.com/terms/',
        contact=openapi.Contact(email='123456789abc@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

# Router setup
router = DefaultRouter()
router.register(prefix='blogtype', viewset=BlogTypeViewSet)
router.register(prefix="features", viewset=FeaturesViewSet)
router.register(prefix="category", viewset=CategoryViewSet)
router.register(prefix="comment", viewset=CommentViewSet)
router.register(prefix="problem", viewset=ProblemViewSet)
router.register(prefix="blog", viewset=BlogViewSet)
router.register(prefix="advisers", viewset=ServicesViewSet)

# URL patterns
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
]
