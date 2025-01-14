from django.contrib import admin   # type: ignore

from .models import Blog

# Register your models here.

@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title"]
    list_display_links = ["id", "user"]
    list_filter = ["user", "title"]
    search_fields = ["user", "title",]
    search_help_text = "You can search only with title, author or category"




