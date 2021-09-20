from django.contrib import admin
from home.models import *
# Register your models here.

class CuVideo(admin.ModelAdmin):
	fields = ('user', 'title', 'desc', 'video_file', 'thumbnail', 'tags')
admin.site.register(Video, CuVideo)

class AdComment(admin.ModelAdmin):
	fields = ('post', 'body', 'name', )
admin.site.register(Comment, AdComment)

class AdLikes(admin.ModelAdmin):
	fields = ('post', 'user')
admin.site.register(Likes, AdLikes)

admin.site.register(Contact)
