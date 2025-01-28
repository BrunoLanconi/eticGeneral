from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at", "published")
    list_filter = ("created_at", "updated_at", "published")
    search_fields = ("title", "content")
    date_hierarchy = "created_at"


admin.site.register(Post, PostAdmin)
