# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite import models

# Register your models here.

admin.site.site_header = "mini个人博客"
admin.site.site_title = "MINIWEBLOG"


class UserAdmin(admin.ModelAdmin):
	list_display=('name','level','sex')
	search_fields=('name',)
	def _str_(self):
		return self.name
admin.site.register(models.User, UserAdmin)

class FriendAdmin(admin.ModelAdmin):
	list_display=('name','sex','hobby','star')
	serch_fields=('name',)
admin.site.register(models.Friend,FriendAdmin)

class PhotoAdmin(admin.ModelAdmin):
	list_display=('name','description','time')
	serch_fields=('name',)
	ordering = ('-time',)
admin.site.register(models.Photo,PhotoAdmin)

class EssayAdmin(admin.ModelAdmin):
	list_display=('title','time','count')
	serch_fields=('title',)
	ordering = ('-time',)
admin.site.register(models.Essay,EssayAdmin)

admin.site.register(models.EssayBack)