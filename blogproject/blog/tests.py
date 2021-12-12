from django.contrib.admin.views import main
from django.test import TestCase

# Create your tests here.
from models import Category,Post,Tag
from django.contrib.auth.models import User
from django.utils import timezone


# c = Category(name='categore test')
# c.save()
# t = Tag(name='tag test')
# t.save()
# user = User.objects.get(username='myuser')
# c_name = Category.objects.get(name='categore test')
# p = Post(title='title test',body='body test',create_time=timezone.now(),modified_time=timezone.now(),category=c_name, author=user)
# p.save()
