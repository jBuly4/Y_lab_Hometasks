from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models

# Register your models here.


class RecipieInline(admin.StackedInline):
    model = models.Recipie
    extra = 1  # number of recipies for 1 post when creating post


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'create_at', 'id']
    inlines = [RecipieInline]  # added possibility to create post + recipie together


@admin.register(models.Recipie)
class RecipieAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.Ingredients)
