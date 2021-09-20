from django.contrib import admin
from django.urls import path, include
from home.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

from home.sitemap import VideoSitemap, PageSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps={
	'videos': VideoSitemap,
	'pages': PageSitemap,
}
urlpatterns = [
    path('letmein/', admin.site.urls),
    path(
    	'sitemap.xml', sitemap, { 'sitemaps':sitemaps}, name="django.contrib.sites.views.sitemap"
    ),
    path('robots.txt', include('robots.urls')),
    path('comments/', addcomm, name="comments"),
    path('privacy_policy', pp, name="pp"),
    path('dmca', dmca, name="dmca"),
    path('contact', contact, name="c"),
    path('tac', tac, name="tac"),
    path('alert/', alert, name="alert"),
    path('about_us', about, name="about"),
    path('', index, name='home'),
    path('watch/<int:id>', watch, name='watch-video'),
    path('send', c, name="cont"),
    path('search/', search, name="search"),
    path('cats/<str:tag>', tagview, name="cats"),
    path('signup/', signup, name="signup"),
    path('login/', hlogin, name="login"),
    path('logout/', hlogout, name="logout"),
    path('liked/<int:id>', liked, name="lik"),
    path('user/<usern>', profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "TiksPorn Admin"
admin.site.site_title = "TiksPorn Admin Portal"
admin.site.index_title = "Welcome to TiksPorn"
