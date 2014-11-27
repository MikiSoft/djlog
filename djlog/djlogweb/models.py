from django.db import models


class PostsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Posts(models.Model):
    title = models.CharField(max_length=200)
    post_author = models.CharField(max_length=40)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostsQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Djlog post"
        verbose_name_plural = "Djlog posts"
        ordering = ["-created_at"]

# Create your models here.
