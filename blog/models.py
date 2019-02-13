from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length = 70)

	body = models.TextField()

	views = models.PositiveSmallIntegerField(default=0)

	created_time = models.DateTimeField()

	modified_time = models.DateTimeField()

	excerpt = models.CharField(max_length = 200, blank = True)
	'''在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
	此参数为了避免两个表里的数据不一致问题，不然会报错：'''
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	tags = models.ManyToManyField(Tag, blank = True)

	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs = {'pk': self.pk})

	class Meta:
		ordering = ['-created_time']

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])