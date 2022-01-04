from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, response
from .models import Post,Category,Tag
import markdown,re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.views.generic import DetailView,ListView
from pure_pagination.mixins import PaginationMixin

# Create your views here.


#主页
# def index(request):
#     post_list = Post.objects.all()
#     return render(request,'blog/index.html',context={
#         'post_list':post_list
#     })
#用类视图重写


class IndexView(PaginationMixin,ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

#详情页
# def detail(request,pk):
#     #引用django.shortcuts模块中的get_object_or_404的方法如果从数据库中匹配到pk就返回数据Post,如果没有就返回404错误界面
#     post = get_object_or_404(Post,pk=pk)
#     #启用markdown语法扩展，将markdown文档解析为html
#     post.increase_views()
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',#基础语法扩展
#         'markdown.extensions.codehilite',#语法高亮扩展
#         # 'markdown.extensions.toc', #容许自动生成目录
#         # 记得在顶部引入 TocExtension 和 slugify
#         TocExtension(slugify=slugify),#美化锚点
#     ])
#     #将数据库中markdown文件解析，一旦调用convert方法，实例md就会多出一个toc属性，这个属性的值就是内容的目录
#     post.body = md.convert(post.body)
#     #用正则匹配md.toc，在detail.html模板做判断是否显示侧面目录，处理空目录
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>',md.toc,re.S)
#     if m is not None:
#         post.toc=m.group(1)
#     else:
#         post.toc=""

#     return render(request,'blog/detail.html',context={'post':post})
#类视图重写
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()
        return response
    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        post.body = md.convert(post.body)
        m = re.search(r'<div class="toc">\s*<url>(.*)</ul>\s*</div>',md.toc,re.S)
        if m is not None:
            post.toc = m.group(1)
        else:
            post.toc = ''
        # post.toc = m.group(1) if m is not None else ''
        return post

#归档详情页
# def archive(request,year,month):
#     post_list = Post.objects.filter(create_time__year=year,create_time__month=month)
#     return render(request,'blog/index.html',context={'post_list':post_list})
#类视图重写
class ArchiveView(IndexView):
    def get_queryset(self):
        return super(ArchiveView,self).get_queryset().filter(create_time__year=self.kwargs.get('year'),create_time__month=self.kwargs.get('month'))
#分类页面
# def category(request,pk):
#     cate = get_object_or_404(Category,pk=pk)
#     post_list = Post.objects.filter(category=cate)
#     return render(request,'blog/index.html',context={'post_list':post_list})
#类视图重写 
class CategoreView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoreView,self).get_queryset().filter(category=cate)


# #标签页面
# def tag(request,pk):
#     t = get_object_or_404(Tag,pk=pk)
#     post_list = Post.objects.filter(tag=t)
#     return render(request,'blog/index.html',context={'post_list':post_list})
#类视图重写
class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tag=t)