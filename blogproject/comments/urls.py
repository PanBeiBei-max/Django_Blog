from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'comments'


urlpatterns = [
    path('comment/<int:post_pk>',views.comment,name='comment'),
]