from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

# MTTP will help to build nested tags and binary trees

class Category(MPTTModel):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150)
    parent = TreeForeignKey(
            'self',
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name="children"
    )

    def __str__(self):
        return self.name

    class MTTPMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
            User,
            related_name="posts",
            on_delete=models.CASCADE
    )
    title = models.CharField(max_length=240)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
            Category,
            related_name='post',
            on_delete=models.SET_NULL,
            null=True
    )
    tag = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detailed", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_recipes(self):
        return self.recipie.all()

    def get_comments(self):
        return self.comment.all()


class Recipie(models.Model):
    name = models.CharField(max_length=120)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    # ingredients = models.TextField()  # should be as table, m2m field
    ingredients = models.ManyToManyField(Ingredients, related_name='recipie')
    instruction = models.TextField()
    post = models.ForeignKey(
            Post,
            related_name='recipie',
            on_delete=models.SET_NULL,
            null=True,
            blank=True
    )

# future features


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=400)
    post = models.ForeignKey(
            Post,
            related_name='comment',
            on_delete=models.CASCADE,  # deleting post we delete all comments
    )

