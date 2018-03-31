# -*-coding:utf8-*-
from django.contrib import admin
from .models import Post, Tag, Category, Comment, CommentPost


# class GlobalSetting(object):
#     site_title = u"博客后台"
#     site_footer = "wersonliu"

# class PostAdmin(object):
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'author']
    search_fields = ['title', 'category', 'tags']
    list_filter = ['created_time', 'category', 'tags']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'text', ]


# class TagAdmin(object):
#     list_display = ['name']
#
#
# class CategoryAdmin(object):
#     list_display = ['name']

class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(CommentPost, CommentPostAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
# xadmin.site.register(Post, PostAdmin)
# xadmin.site.register(Tag)
# xadmin.site.register(Category)
