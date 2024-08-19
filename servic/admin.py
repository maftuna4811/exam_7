from django.contrib import admin
from .models import Features, Services, Blog, Category, BlogType
from import_export.admin import ImportExportModelAdmin

# admin.site.register([Address, Apartment, City, Category, SellType])


@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ['category', 'short_name', 'features', 'description']
    list_display_links = ['category', 'short_name', 'features', 'description']
    search_fields = ['category', 'short_name', 'features', 'description']


@admin.register(Features)
class FeaturesAdmin(ImportExportModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ['name', 'image', 'blog_type']
    list_display_links = ['name', 'image', 'blog_type']
    search_fields = ['name', 'image', 'blog_type']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'views']
    list_display_links = ['name', 'views']
    search_fields = ['name', 'views']


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
