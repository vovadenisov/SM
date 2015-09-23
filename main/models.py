from django.db import models
from sortedm2m.fields import SortedManyToManyField
from ckeditor.fields import RichTextField
from photologue.models import Photo, Gallery
import datetime

#http://djbook.ru/rel1.6/ref/models/fields.html

class Departments(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	name = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	#gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	article = SortedManyToManyField('Articles', blank = True)
	content = RichTextField()
	template = models.CharField(max_length=50, default='base_department.html')
	def __unicode__(self):
		return self.short_name

class Partner(models.Model):
	short_name = models.CharField(max_length=100)
        title = models.CharField(max_length=100)
        content = models.TextField(blank=True)
        link = models.CharField(max_length=100)
        photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
        def __udicode__(self):
                return self.short_name

class Units(models.Model):
        short_name = models.CharField(max_length=50, unique = True)
        name = models.CharField(max_length=250)
        description = models.TextField(blank=True)
        photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
        #gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
        article = SortedManyToManyField('Articles', blank = True)
        #content = RichTextField()
	url = models.CharField(max_length=150)
	def __unicode__(self):
                return self.short_name

class Didjest_theme(models.Model):
	title = models.CharField(max_length = 250)
	def __unicode__(self):
		return self.title

class Didjest_year(models.Model):
        year = models.CharField(max_length=30)
        theme = models.ForeignKey(Didjest_theme)
        def __unicode__(self):
		name = self.year + " " + self.theme.title
                return name

class Didjest(models.Model):
	name = models.CharField(max_length=150)
	link = models.CharField(max_length=250)
	number = models.IntegerField()
	year = models.ForeignKey(Didjest_year)
	def __unicode__(self):
                return self.name	

class Youth_project(models.Model):
	short_name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	link = models.CharField(max_length=100)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	def __unicode__(self):
		return self.short_name 

class decanTime(models.Model):
	date = models.CharField(max_length=50)
	decan = models.TextField(blank=True)
	def __unicode__(self):
		return self.date

class Publication(models.Model):
	pub_img = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	pub_name = models.CharField(max_length=150)
	pub_autor = models.CharField(max_length=150)
	pub_date = models.DateTimeField(default=datetime.datetime.now())
	content = models.CharField(max_length=450)
	pub_link = models.CharField(max_length=150)
	def __unicode__(self):
		return self.pub_name

class Projects(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	name = models.CharField(max_length=250)
	isFavorite = models.BooleanField(default=True)
	description = models.TextField()
	department = models.ForeignKey(Departments, blank=True, null=True, on_delete=models.SET_NULL)
	article = SortedManyToManyField('Articles', blank = True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	#gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	content = RichTextField()
	template = models.CharField(max_length=50, default='base_project.html')
	def __unicode__(self):
		return self.short_name

class Articles(models.Model):
	short_name = models.CharField(max_length=50, unique = True)
	title = models.CharField(max_length=250)
	subtext = models.CharField(max_length=250, blank = True)
	author = models.CharField(max_length=250)
	pub_date = models.DateTimeField(default=datetime.datetime.now())
	isFavorite = models.BooleanField(default=True)
	description = RichTextField()
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	#gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	content = RichTextField()
	template = models.CharField(max_length=50, default='base_article.html')
	def __unicode__(self):
		return self.short_name

class About_Decan(models.Model):
	title = models.CharField(max_length = 50)
	content = RichTextField()
	def __unicode__(self):
		return self.title

class Decan_text(models.Model):
        title = models.CharField(max_length = 50)
        content = RichTextField()
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
        def __unicode__(self):
                return self.title

class News(models.Model):
	title = models.CharField(max_length=250)
	isFavorite = models.BooleanField(default=True)
	description = models.TextField(blank=True)
	pub_date = models.DateTimeField(default=datetime.datetime.now())
	article = SortedManyToManyField(Articles, blank = True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	content = RichTextField()
	template = models.CharField(max_length=50, default='base_news.html')
	def __unicode__(self):
		return self.title

	def getPubDate(self):
		return self.pub_date.strftime("%Y.%m.%d %H:%M:%S")

class AboutBMSTU(models.Model):
	title = models.CharField(max_length=250)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	#gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	article = SortedManyToManyField(Articles, blank = True)
	history_title = models.CharField(max_length=250)
	history_text = RichTextField(blank=True)
	history_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	history_gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	facts_title = models.CharField(max_length=250)
	facts_text = RichTextField(blank=True)
	facts_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	facts_gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	tradition_title = models.CharField(max_length=250)
	tradition_text = RichTextField(blank=True)
	tradition_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	tradition_gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')	
	tree_title = models.CharField(max_length=250)
	tree_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	graduates_title = models.CharField(max_length=250, blank = True)
	graduates = SortedManyToManyField('Persons', blank = True)
	def __unicode__(self):
		return self.title

class Phones(models.Model):
	phone_number = models.CharField(max_length=250)
	def __unicode__(self):
		return self.phone_number

class Emails(models.Model):
	email = models.CharField(max_length=250)
	def __unicode__(self):
		return self.email

class Addresses(models.Model):
	address = models.CharField(max_length=250)
	def __unicode__(self):
		return self.address

class Persons(models.Model):
	full_name = models.CharField(max_length=250)
	text = models.TextField(blank=True)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	def __unicode__(self):
		return self.full_name

class Contacts(models.Model):
	title = models.CharField(max_length=250)
	photo_map = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	phone_number = SortedManyToManyField(Phones, blank = True)
	addresses = SortedManyToManyField(Addresses, blank = True)
	emails = SortedManyToManyField(Emails, blank = True)
	contact_information = models.TextField(blank=True)
	bank_details = RichTextField(blank=True)
	contactees = SortedManyToManyField(Persons, blank = True)
	def __unicode__(self):
		return self.title

class Banners(models.Model):
	name = models.CharField(max_length=250)
	photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
	url = models.CharField(max_length=250)
	def __unicode__(self):
		return self.name






















