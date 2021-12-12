from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag
import markdown,re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

# Create your views here.


#主页
def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={
        'post_list':post_list
    })

#详情页
def detail(request,pk):
    #引用django.shortcuts模块中的get_object_or_404的方法如果从数据库中匹配到pk就返回数据Post,如果没有就返回404错误界面
    post = get_object_or_404(Post,pk=pk)
    #启用markdown语法扩展，将markdown文档解析为html
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',#基础语法扩展
        'markdown.extensions.codehilite',#语法高亮扩展
        # 'markdown.extensions.toc', #容许自动生成目录
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),#美化锚点
    ])
    #将数据库中markdown文件解析，一旦调用convert方法，实例md就会多出一个toc属性，这个属性的值就是内容的目录
    post.body = md.convert(post.body)
    #用正则匹配md.toc，在detail.html模板做判断是否显示侧面目录，处理空目录
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>',md.toc,re.S)
    if m is not None:
        post.toc=m.group(1)
    else:
        post.toc=""

    return render(request,'blog/detail.html',context={'post':post})


#归档详情页
def archive(request,year,month):
    post_list = Post.objects.filter(create_time__year=year,create_time__month=month)
    return render(request,'blog/index.html',context={'post_list':post_list})


#分类页面
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})


#标签页面
def tag(request,pk):
    t = get_object_or_404(Tag,pk=pk)
    post_list = Post.objects.filter(tag=t)
    return render(request,'blog/index.html',context={'post_list':post_list})