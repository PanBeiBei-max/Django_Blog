from django.db import models
from django.utils import timezone
# Create your models here.



class Comment(models.Model):
    #用户名字
    name = models.CharField(verbose_name='名字',max_length=50)
    #用户的电子邮箱
    email = models.EmailField(verbose_name='邮箱')
    #用户的个人网站，可以为空
    url = models.URLField(verbose_name='网址',blank=True)
    #评论内容
    text = models.TextField(verbose_name='内容')
    #该评论创建时间
    created_time = models.DateTimeField(verbose_name='创建时间',default=timezone.now)
    #关联blogapp的Post文章表，级联删除
    post = models.ForeignKey('blog.Post',verbose_name='文章',on_delete=models.CASCADE)


    class Meta:
        verbose_name = '评论'
        #指定该表在admin后台显示的复数形式
        verbose_name_plural = verbose_name
        ordering = ['-created_time','name']
    
    def __str__(self):
        return '{}:{}'.format(self.name,self.text[:20])