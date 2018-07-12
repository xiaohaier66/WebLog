# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpResponse, Http404,HttpResponseRedirect
from mysite import models
from django.template import RequestContext, Template
from django.template.context_processors import csrf

# Create your views here.
	
from mysite import models, forms
def contact(request):
	if request.user.is_authenticated(): 
		if request.method == 'POST':
			form = forms.ContactForm(request.POST)
			if form.is_valid():
				message = "感谢您的来信。"
				user_name = form.cleaned_data['user_name']
				user_city = form.cleaned_data['user_city']
				user_school = form.cleaned_data['user_school']
				user_email = form.cleaned_data['user_email']
				user_message = form.cleaned_data['user_message']
			else:
				message = "请检查您输入的信息是否正确！"
		else:
			form = forms.ContactForm()

		csrf(request)
		return render(request,'contact.html',locals())
	else: 
		return HttpResponseRedirect('/admin/')
	
	
from django.http import HttpResponse, HttpResponseRedirect

def base2(request):
	template = get_template('base2.html')
	
	html = template.render(locals())
	
	return HttpResponse(html)

from .models import Friend
def friend(request):
	template = get_template('friend.html')
	friends = Friend.objects.all()
	html = template.render(locals())
	return HttpResponse(html)
	
from .models import Essay
from datetime import datetime
def article(request):
	template = get_template('article.html')
	articles = Essay.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)

from .models import Photo
def photo(request):
	template = get_template('photo.html')
	photos = Photo.objects.all()
	html = template.render(locals())
	return HttpResponse(html)
	
from .models import EssayBack
def index(request):
	template = get_template('index.html')
	essaybacks = EssayBack.objects.all()
	html = template.render(locals())
	return HttpResponse(html)
	
from .models import Essay
def article_detail(request, id ):
	template = get_template('article_detail.html')
	try:
		essay = Essay.objects.get(id = id)
	except Essay.DoesNotExist:
		return Http404('找不到该文章')
	html = template.render(locals())
	return HttpResponse(html)
	
from .models import Friend
def friend_detail(request, id ):
	template = get_template('friend_detail.html')
	try:
		friend = Friend.objects.get(id = id)
	except Friend.DoesNotExist:
		return Http404('找不到该好友')
	html = template.render(locals())
	return HttpResponse(html)
	
from .models import Photo
def photo_detail(request, id ):
	template = get_template('photo_detail.html')
	try:
		photo = Photo.objects.get(id = id)
	except Photo.DoesNotExist:
		return Http404('找不到该图片')
	html = template.render(locals())
	return HttpResponse(html)
	
from mysite import models, forms
def article_post(request):
	if request.method == 'POST':
		form = forms.ArticlePostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			user_name = form.cleaned_data['user_name']
			essay_type = form.cleaned_data['essay_type']
			content = form.cleaned_data['content']
			time = datetime.now()
			count = 1
			id = form.cleaned_data['id']
			form.save()
			return HttpResponseRedirect('/article/')
		else:
			message = "请检查您输入的信息是否正确！"
	else:
		form = forms.ArticlePostForm()

	csrf(request)
	return render(request,'article_post.html',locals())
	
def friend_post(request):
	if request.method == 'POST':
		form = forms.FriendPostForm(request.POST)
		
		if form.is_valid():
			name = form.cleaned_data['name']
			user_name = form.cleaned_data['user_name']
			discription = form.cleaned_data['discription']
			sex = form.cleaned_data['sex']
			address = form.cleaned_data['address']
			email = form.cleaned_data['hobby']
			star = form.cleaned_data['star']
			id = form.cleaned_data['id']
			form.save()
			return HttpResponseRedirect('/friend/')
		else:
			message = "请检查您输入的信息是否正确！"
	else:
		form = forms.FriendPostForm()

	csrf(request)
	return render(request,'friend_post.html',locals())
	
def photo_post(request):
	if request.method == 'POST':
		form = forms.PhotoPostForm(request.POST)
		
		fields = ['name','user_name','path','description','id']
		
		if form.is_valid():
			name = form.cleaned_data['name']
			user_name = form.cleaned_data['user_name']
			path = form.cleaned_data['path']
			description = form.cleaned_data['description']
			time = datetime.now()
			id = form.cleaned_data['id']
			form.save()
			return HttpResponseRedirect('/photo/')
		else:
			message = "请检查您输入的信息是否正确！"
	else:
		form = forms.PhotoPostForm()

	csrf(request)
	return render(request,'photo_post.html',locals())
	
from django.shortcuts import redirect
def login(request):
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)		
		if login_form.is_valid():
			login_name = request.POST['username'].strip()
			login_password = request.POST['password']
			try:
				user = models.User.objects.get(name=login_name)
				if user.password == login_password:
					#return HttpResponseRedirect('/index/')
					csrf(request)
					return render(request,'/index/',locals())
			except:
				message = "无法登录"
			
		else:
			message = "请检查输入的字段内容"
	else:
		login_form = forms.LoginForm()
	
	csrf(request)
	return render(request,'login.html',locals())
	
def base(request):
	template = get_template('base2.html')
	html = template.render(locals())
	return HttpResponse(html)