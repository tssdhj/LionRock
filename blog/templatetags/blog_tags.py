from ..models import Post, Tag, Category
from django.db.models.aggregates import Count
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=3):
	return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
	return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
	#返回所有的分类，这里是不合理的，有些分类下面可能还没有文章存在
	#return Category.objects.all()
	#过滤掉文章数为零的分类
	return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
	#return Tag.objects.all()
	return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)