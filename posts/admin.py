from django.contrib import admin
from .models import Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ["title", "published", "updated"]
    list_filter = ["published"]
    search_fields = ["text"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)