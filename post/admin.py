from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title',)
    filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
