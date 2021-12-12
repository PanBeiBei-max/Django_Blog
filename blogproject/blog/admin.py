from django.contrib import admin
from django.db.models import fields
from .models import Category,Tag,Post
# Register your models here.

#文章分类admin界面显示与操作
class PostAdmin(admin.ModelAdmin):
    #在后台界面显示标题，创建时间，修改时间，分类，作者
    list_display = ['title','create_time','modified_time','category','author']
    #在后台添加修改界面只显示一下字段[标题，内容，摘要，分类，标签]
    fields = ['title','body','excerpt','category','tag']
    #绑定Post实例的作者为后台登录的作者
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)
#将数据库中的表注册进admin，将设置注册进admin，其中PostAdmin类为Post表的设置
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
