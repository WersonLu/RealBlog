# encoding: utf-8
# !/usr/bin/env python


'''
@author  : wersonliu
@File    : forms.py
@data    : 
'''

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

