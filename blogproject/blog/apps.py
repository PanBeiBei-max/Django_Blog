from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    #在django后台显示中文“博客”
    verbose_name = '博客'
