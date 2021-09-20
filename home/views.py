from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from home.models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
	vids= Video.objects.all().order_by('-id')
	paginator= Paginator(vids,20)
	page_num=request.GET.get('page', 1)
	vids= paginator.page(page_num)
	
	context={'vids':vids}
	return render(request, 'home.html', context)
	
	
	
def watch(request, id):
	vid = Video.objects.get(pk=id)
	allcom = Comment.objects.filter(post=vid)
	atags = vid.tags.all()
	rp =Video.objects.filter( tags__in=atags).order_by('-pub_date').exclude(pk=id)[:6]
	
	
	context={'vid':vid, 'allcom':allcom, 'rp':rp}
	return render(request, 'watch.html', context)
	


def addcomm(request):
	if request.method == 'POST':
		body = request.POST['com']
		name = request.POST['nam']
		
		spost = request.POST['sno']
		post = Video.objects.get(id=spost)
		cm = Comment(body=body, name=name, post=post)
		cm.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def search(request):
		if request.method == 'POST':
			query = request.POST['srch']
			searched = Video.objects.filter(title__icontains=query)
			
			context={
					'query':query,
					'sr':searched
			}
			return render(request, 'search.html', context)



def profile(request, usern):
	usr = User.objects.get(username=usern)
	uv = Video.objects.filter(user=usr)
	paginator= Paginator(uv,8)
	page_num=request.GET.get('page', 1)
	uv= paginator.page(page_num)
	
	context={'uv':uv, 'usr':usr}
	return render(request, 'profile.html', context)
	
@login_required(login_url='/alert/')
def liked (request, id):
	user = request.user
	post = Video.objects.get(id=id)
	current_likes = post.likes
	
	likedd = Likes.objects.filter(user=user, post=post).count()
	
	if not likedd:
		like = Likes.objects.create(user=user, post=post)
		like.save()
		current_likes= current_likes + 1
	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes= current_likes - 1
	post.likes = current_likes
	post.save()
		
		
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def alert(request):
	return render (request, 'lr.html')
def dmca(request):
	return render (request, 'dmca.html')
def tac(request):
	return render(request, 'tac.html')
def contact(request):
	return render(request, 'contact.html')

def c(request):
	if request.method == 'POST':
		con = Contact()
		con.n = request.POST['name']
		con.e = request.POST['mail']
		con.t = request.POST['text']
		con.save()
		messages.info(request, "Message sent successfully, we will replied to your email.")
		return redirect(contact)
