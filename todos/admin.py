from django.contrib import admin
from todos.models import Tag, TODO


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "level", "due_date", "status"]
