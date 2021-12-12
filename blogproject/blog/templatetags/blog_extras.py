from django import template
from ..models import Post,Category,Tag



#实例化一个template.Library类
register = template.Library()

#最新文章模板
#将函数 show_recent_posts 装饰为 register.inclusion_tag，这样就告诉 django，这个函数是我们自定义的一个类型为 inclusion_tag 的模板标签
#inclusion_tag 装饰器的参数 takes_context 设置为 True 时将告诉 django，在渲染 _recent_posts.html 模板时，不仅传入show_recent_posts 
#返回的模板变量，同时会传入父模板（即使用 {% show_recent_posts %} 模板标签的模板）上下文
@register.inclusion_tag('blog/inclusions/_recent_posts.html',takes_context=True)
def show_recent_posts(context,num=5):
    #返回一个字典值，字典中的值将作为模板变量，传入由 inclusion_tag 装饰器第一个参数指定的模板。当我们在模板中通过 {% show_recent_posts %}
    #使用自己定义的模板标签时，django 会将指定模板的内容使用模板标签返回的模板变量渲染后替换
    return {
        'recent_post_list':Post.objects.all()[:num],
    }

#归档模板
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    #这里Post.objects.dates方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间（已去重），且是Python的date对象，精确到月份，降序排列
    return {
        'date_list': Post.objects.dates('create_time', 'month', order='DESC'),
    }

#分类模板
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = []
    for cate in Category.objects.all():
        num = len(Post.objects.filter(category=cate.pk))
        category_list.append([cate.name,num,cate.pk])
    return {
        # 'category_list':Category.objects.all(),
        'category_list':category_list
        # 'category_num':len(Post.objects.filter()),
    }

#标签模板
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }