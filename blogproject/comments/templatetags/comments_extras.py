from django import forms, template
from ..forms import CommentForm



register = template.Library()

@register.inclusion_tag('comments/inclusions/_form.html',takes_context=True)
def show_comment_form(context,post,form=None):
    if form is None:
        form = CommentForm()
    return {
        'form':form,
        'post':post,
    }


@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    #这里 post.comment_set.all() 也等价于 Comment.objects.filter(post=post)，即根据 post 来过滤该 post 下的全部评论
    comment_list = post.comment_set.all()
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }