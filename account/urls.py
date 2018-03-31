# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : urls.py
@data    : 
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^logout-then-login/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),
]
