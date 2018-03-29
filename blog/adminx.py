# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : adminx.py
@data    : 
'''

import xadmin

# from xadmin import views
from .models import Post, Tag, Category


class GlobalSetting(object):
    site_title = "博客后台"
    site_footer = "wersonliu"


class PostAdmin(object):
    list_display = ['title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author']
    search_fields = ['title', 'category', 'tags']
    list_filter = ['created_time', 'category', 'tags']


class TagAdmin(object):
    list_display = ['name']


class CategoryAdmin(object):
    list_display = ['name']


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
