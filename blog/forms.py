# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : forms.py
@data    : 
'''
from django import forms
from .models import Comment, CommentPost


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'text']


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('name', 'email', 'body')
