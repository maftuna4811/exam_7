from django.contrib import admin

from django.contrib import admin
from .models import Advisers, Problems, Comments
from import_export.admin import ImportExportModelAdmin
# admin.site.register([Agents, Problems, Comments])


@admin.register(Problems)
class ProblemsAdmin(ImportExportModelAdmin):
    list_display = ['firstname', 'email', 'problem_name']
    list_display_links = ['firstname', 'email', 'problem_name']
    search_fields = ['firstname', 'email', 'problem_name']


@admin.register(Advisers)
class AgentsAdmin(ImportExportModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'views']
    list_display_links = ['firstname', 'lastname', 'email', 'views']
    search_fields = ['firstname', 'lastname', 'email', 'views']


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ['user', 'comment_title']
    list_display_links = ['user', 'comment_title']
    search_fields = ['comment_title']
