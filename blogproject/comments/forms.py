from django import forms
from django.db import models
from django.db.models import fields #导入django的表单form功能
from .models import Comment


#django的表单类必须继承自forms.Form类或者forms.ModelForm类。如果表单对应有一个数据库模型，那么使用ModelForm类会简单很多
class CommentForm(forms.ModelForm):

    class Meta:
        #表明这个表单对应的数据库模型是Comment类
        model = Comment
        #指定了表单显示的字段
        fields = ['name','email','url','text']