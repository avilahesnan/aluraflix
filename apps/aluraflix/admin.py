from django.contrib import admin
from apps.aluraflix.models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_filter = ('type',)
    list_per_page = 10
    ordering = ('title',)
