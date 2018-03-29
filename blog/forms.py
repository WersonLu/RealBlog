# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : forms.py
@data    : 
'''
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'text']
