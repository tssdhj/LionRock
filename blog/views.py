from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag, Category
from comments.forms import CommentForm
import markdown

# Create your views here.
def index(request):
	#return HttpResponse('hello dddddddworld')
	"""return render(request, 'blog/index.html', context = {
			'title': 'lion rock',
			'welcome': 'tssdhj    hhhhhhhh'
		})"""
	post_list = Post.objects.all()
	return render(request, 'blog/index.html', context = {'post_list': post_list})

def detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	post.body = markdown.markdown(post.body, 
			extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
				'markdown.extensions.toc'
			])
	form = CommentForm()
	comment_list = post.comment_set.all()
	context = {
		'post': post,
		'form': form,
		'comment_list': comment_list
	}
	return render(request, 'blog/detail.html', context = context)

#根据归档时间查询文章
#g改为USE_TZ = False
def archives(request, year, month):
	post_list = Post.objects.filter(created_time__year = year,
		created_time__month = month)
	return render(request, 'blog/index.html', context = {'post_list': post_list})

#根据标签查询出所有文章
def category(request, pk):
	cate = get_object_or_404(Category, pk = pk)
	post_list = Post.objects.filter(category = cate)
	total = len(post_list)
	print(total)
	return render(request, 'blog/index.html', context = {'post_list': post_list,'total': total})

def tag(request,pk):
	tag = get_object_or_404(Tag, pk = pk)
	post_list = Post.objects.filter(tags = tag)
	return render(request, 'blog/index.html', context = {
			'post_list': post_list})