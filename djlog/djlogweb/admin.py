from django.contrib import admin
from . import models


class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Posts, PostsAdmin)
admin.site.register(models.Tag)
# Register your models here.
