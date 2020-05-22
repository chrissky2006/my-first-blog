# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:24:05 2020

@author: Administrator
"""


from django.urls import path
from . import views

urlpatterns=[
    path('',views.post_list,name='post_list')
    ]