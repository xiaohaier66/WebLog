#_*_ encoding: utf-8 *_*
from django import forms
from mysite import models

class ContactForm(forms.Form):
	CITY = [
		['TP', 'Taipei'],
		['TY', 'Taoyuang'],
		['TC', 'Taichung'],
		['TN', 'Tainan'],
		['KS', 'Kaohsiung'],
		['NA', 'Others'],
	]
	user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')
	user_city = forms.ChoiceField(label='居住城市', choices=CITY)
	user_school = forms.BooleanField(label='是否在学', required=False)
	user_email = forms.EmailField(label='电子邮件')
	user_message = forms.CharField(label='您的意见', widget=forms.Textarea)

	
class ArticlePostForm(forms.ModelForm):
	class Meta:
		model = models.Essay
		fields = ['title','user_name','essay_type','content','id']
		
		def __init__(self, *args, **kwargs):
			super(ArticlePostForm, self).__init__(*args, **kwargs)
			self.fields['title'].label = '标题'
			self.fields['user_name'].label = '发表人'
			self.fields['essay_type'].label = '文章类型'
			self.fields['content'].label = '文章内容'
			self.fields['id'].label = '编号'
			
class FriendPostForm(forms.ModelForm):
	class Meta:
		model = models.Friend
		fields = ['name','user_name','discription','sex','address','email','hobby','star','id']
		
		def __init__(self, *args, **kwargs):
			super(FriendPostForm, self).__init__(*args, **kwargs)
			self.fields['name'].label = '用户'
			self.fields['user_name'].label = '姓名'
			self.fields['discription'].label = '描述'
			self.fields['sex'].label = '性别'
			self.fields['address'].label = '住址'
			self.fields['email'].label = '电子邮箱'
			self.fields['hobby'].label = '兴趣'
			self.fields['star'].label = '星座'
			self.fields['id'].label = '编号'
			
class PhotoPostForm(forms.ModelForm):
	class Meta:
		model = models.Photo
		fields = ['name','user_name','path','description','id']
		
		def __init__(self, *args, **kwargs):
			super(PhotoPostForm, self).__init__(*args, **kwargs)
			self.fields['name'].label = '标题'
			self.fields['user_name'].label = '发表人'
			self.fields['path'].label = '图片路径'
			self.fields['description'].label = '描述'
			self.fields['id'].label = '编号'
			
class LoginForm(forms.Form):
	username =  forms.CharField(label='姓名', max_length=10)
	password = forms.CharField(label='密码', widget=forms.PasswordInput())