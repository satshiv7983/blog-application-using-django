# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:47:12 2021

@author: MY LENOVO
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField() 
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField() 
    
    class Meta:
        model=User
        fields=['username','email']
        
    
class ProfileUpdateForm(forms.ModelForm):
        
    class Meta:
        model=Profile
        fields=['image']
    
    
    
    
    
    
    
        
        
