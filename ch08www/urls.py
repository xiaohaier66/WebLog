"""ch08www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^contact/$',views.contact),
	url(r'^base2/$',views.base2),
	url(r'^friend/$',views.friend),
	url(r'^article/$',views.article),
	url(r'^photo/$',views.photo),
	url(r'^login/$',views.login),
	url(r'^$',views.index),
	url(r'^article/(\d+)/$',views.article_detail,name='article-detail-url'),
	url(r'^friend/(\d+)/$',views.friend_detail,name='friend-detail-url'),
	url(r'^photo/(\d+)/$',views.photo_detail,name='photo-detail-url'),
	url(r'^article_post/$',views.article_post,name='article-post-url'),
	url(r'^friend_post/$',views.friend_post,name='friend-post-url'),
	url(r'^photo_post/$',views.photo_post,name='photo-post-url'),
	url(r'^base/$',views.base,name='base-url'),
]
