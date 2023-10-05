from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("created_at", "deadline", "is_done")
    search_fields = ("tags",)
    list_filter = (
        "tags",
        "created_at",
        "tags",
        "created_at",
        "deadline",
        "is_done",
    )
