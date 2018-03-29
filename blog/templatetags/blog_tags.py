# -*-coding:utf8-*-
# !/usr/bin/env python

from ..models import Post, Category, Tag, Comment
from django.db.models.aggregates import Count
from django import template

register = template.Library()


@register.simple_tag
# 获取日期倒序5篇文章
def get_recent_post(nums=5):
    return Post.objects.all().order_by('-created_time')[:nums]


@register.simple_tag
def get_comment():
    return Comment.objects.all().order_by('-created_time')


# @register.simple_tag
# # 获取日期归档下所有
# def gui_dang():
#     return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def fen_lei():
    # 获取某类下所有
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


# 获取标签下的
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
