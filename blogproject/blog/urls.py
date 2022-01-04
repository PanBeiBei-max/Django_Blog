#blogApp下的路由
from django.urls import path
from . import views

#声明App名字
app_name = 'blog'

#此App路由与项目路由拼接
urlpatterns = [
    #path("url地址",views中的方法,声明name)声明name实现动态urls，在django内部别的地方调用，<int:pk>int为数据类型，pk为关键字，动态urls
    # path('',views.index,name='index'),
    # path('posts/<int:pk>/',views.detail,name='detail'),
    # path('archives/<int:year>/<int:month>',views.archive,name='archive'),
    # path('category/<int:pk>',views.category,name='category'),
    # path('tag/<int:pk>',views.tag,name='tag'),
    path('',views.IndexView.as_view(),name='index'),
    path('posts/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('archives/<int:year>/<int:month>',views.ArchiveView.as_view(),name='archive'),
    path('category/<int:pk>',views.CategoreView.as_view(),name='category'),
    path('tag/<int:pk>',views.TagView.as_view(),name='tag'),
]