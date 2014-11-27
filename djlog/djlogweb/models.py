from django.db import models


class PostsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


# Tag model, for storing tags from posts
# It has ManyToMany relation with posts, because one post can have many tags,
# and also one tags can have many posts.

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


# This is a Posts model, which contain logicaly all of the Posts
# Slug is what we are going to use to create URLS. Slug basicly in our example
# takes TITLE, than convert it to lowercase, and replaces whitespaces with '-'
# Example: post titled as "This is stupied" will have a slug "this-is-stupied"

class Posts(models.Model):
    title = models.CharField(max_length=200)
    post_author = models.CharField(max_length=40)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Implementation of Post tags with manytomany relation with Tag model
    tags = models.ManyToManyField(Tag)

    # manging Post quert set with Posts object
    objects = PostsQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Djlog post"
        verbose_name_plural = "Djlog posts"
        ordering = ["-created_at"]

