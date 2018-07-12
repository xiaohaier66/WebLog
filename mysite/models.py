# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Essay(models.Model):
    title = models.CharField(primary_key=True, max_length=45, verbose_name='标题')
    user_name = models.ForeignKey('User', models.DO_NOTHING, db_column='user_name', verbose_name='发表人')
    essay_type = models.CharField(max_length=45, blank=True, null=True, verbose_name='文章类型')
    content = models.TextField(verbose_name='文章内容')
    time = models.DateTimeField(blank=True, null=True, verbose_name='发表时间')
    count = models.IntegerField(blank=True, null=True, verbose_name='访问次数')
    id = models.IntegerField(unique=True, verbose_name='编号')

    class Meta:
        db_table = 'essay'
        unique_together = (('title', 'user_name'),)
	verbose_name_plural = "文章"	


class EssayBack(models.Model):
    friend_name = models.ForeignKey('Friend', models.DO_NOTHING, db_column='friend_name',verbose_name='回复人')
    essay_title = models.ForeignKey(Essay, models.DO_NOTHING, db_column='essay_title',verbose_name='回复的文章')
    content = models.TextField(verbose_name='回复内容')
    time = models.DateTimeField(blank=True, null=True,verbose_name='回复时间')
    id = models.IntegerField(unique=True, verbose_name='编号', primary_key=True)

    class Meta:
        db_table = 'essay_back'
        unique_together = (('essay_title', 'friend_name'),)
	verbose_name_plural = "回复"

class Friend(models.Model):
    name = models.CharField(primary_key=True, max_length=45, verbose_name='姓名')
    user_name = models.ForeignKey('User', models.DO_NOTHING, db_column='user_name', verbose_name='好友关系')
    discription = models.TextField(blank=True, null=True,verbose_name='简介')
    sex = models.CharField(max_length=2,verbose_name='性别')
    address = models.CharField(max_length=45, blank=True, null=True,verbose_name='住址')
    email = models.CharField(max_length=45, blank=True, null=True,verbose_name='电子邮箱')
    hobby = models.CharField(max_length=45, blank=True, null=True, verbose_name='爱好')
    star = models.CharField(max_length=45, blank=True, null=True, verbose_name='星座')
    id = models.IntegerField(unique=True, verbose_name='编号')

    class Meta:
        db_table = 'friend'
        unique_together = (('name', 'user_name'),)
	verbose_name_plural = "好友"



class Photo(models.Model):
    name = models.CharField(primary_key=True, max_length=45,verbose_name='名称')
    user_name = models.ForeignKey('User', models.DO_NOTHING, db_column='user_name',verbose_name='张贴人')
    path = models.CharField(max_length=45,verbose_name='存储路径')
    description = models.TextField(blank=True, null=True,verbose_name='描述')
    time = models.DateTimeField(blank=True, null=True,verbose_name='张贴时间')
    id = models.IntegerField(unique=True, blank=True, null=True,verbose_name='编号')

    class Meta:
        db_table = 'photo'
        unique_together = (('name', 'user_name'),)
	verbose_name_plural = "相册"


class User(models.Model):
    name = models.CharField(primary_key=True, max_length=45, verbose_name='姓名')
		
    level = models.CharField(max_length=5, verbose_name='管理级别')
    sex = models.CharField(max_length=2,verbose_name='姓名')
    password = models.CharField(max_length=16,verbose_name='密码')
    email = models.CharField(max_length=45, blank=True, null=True,verbose_name='电子邮箱')
    address = models.CharField(max_length=45, blank=True, null=True,verbose_name='住址')
    id = models.IntegerField(unique=True,verbose_name='编号')
	
	
    class Meta:
        db_table = 'user'
	verbose_name_plural = "用户"
	
	def _str_(self):
		return self.name
	