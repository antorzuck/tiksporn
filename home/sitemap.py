from django.contrib.sitemaps import Sitemap
from .models import Video
from django.urls import reverse
from home.views import *
from accounts.views import *

 
class VideoSitemap(Sitemap):
	 changefreq = 'weekly'
	 priority = 0.9
	 def items(self):
	 	return Video.objects.all()
          
	 def lastmod(self, obj):
	 	return obj.pub_date
	 
	 def location(self,obj):
	 	return '/watch/%s' % (obj.id)
	 	
class PageSitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['c', 'dmca', 'tac','about', 'pp']

    def location(self, item):
        return reverse(item)
	 