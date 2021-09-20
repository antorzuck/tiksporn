from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from taggit.managers import TaggableManager
# Create your models here.

class Video(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	desc = models.TextField()
	video_file = models.FileField(upload_to='videos/')
	thumbnail = models.FileField(upload_to='videos/thumbnail/')
	pub_date = models.DateField(auto_now_add=True)
	tags = TaggableManager()
	likes = models.IntegerField(default=0)
	video_views = models.ManyToManyField(User, related_name='video_views')

	def __str__(self):
		return self.title
		
		
class Comment(models.Model):
	body = models.TextField()
	name = models.CharField(max_length=20)
	post = models.ForeignKey(Video, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	date = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return self.name
		
		
class Likes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name= 'user_like')
	post = models.ForeignKey(Video, on_delete=models.CASCADE, related_name= 'post_likes')
	def __str__(self):
		return self.user
	
class Contact(models.Model):
	n = models.CharField(max_length=50)
	e = models.CharField(max_length=50)
	t = models.TextField()
	
	def __str__(self):
		return self.e
	
	
	
