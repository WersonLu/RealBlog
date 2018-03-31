# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : urls.py
@data    : 
'''
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from blog.views import IndexView, ShowComment

app_name = 'blog'
urlpatterns = [
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # 博客列表页
    url(r'^blog/$', IndexView.as_view(), name='blog_list'),
    # 文章详情页
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detail'),

    # 分类页
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),

    # 标签页
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tag, name='tag'),
    # 留言页,处理右侧留言
    url(r'^messgae/$', ShowComment.as_view(), name='message'),
    # 留言页　，处理左侧表单
    # url(r'^message/$', MessageView.as_view(), name='message_form'),
    # 留言页详情
    url(r'^comment/(?P<pk>[0-9]+)/$', views.msg_detail, name='msg')
]
