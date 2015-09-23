from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *
import datetime

#http://djbook.ru/rel1.6/topics/db/queries.html

def index(request):
	#newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
	projectsList = Projects.objects.filter(isFavorite = True)[:10]
	memorandum = get_object_or_404(Articles, short_name__iexact = 'memorandum')
	youth = Youth_project.objects.all()
	gallery = get_object_or_404(Gallery, slug__iexact = 'main_page')
	g = gallery.latest(limit=3, public=True)
	units = Units.objects.all()
	partner = Partner.objects.all()
	context = {
		'units': units,
		'isIndex': True,
		'youth': youth,
		'partner':partner,
	#	'newsList': newsList,
		'projectsList': projectsList,
		'gallery': g,
		'memorandum': memorandum
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_index.html', context)

def abitu(request):
        #newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
        decan = Decan_text.objects.all().first
	projectsList = Projects.objects.filter(isFavorite = True)[:10]
        memorandum = get_object_or_404(Articles, short_name__iexact = 'memorandum')
        gallery = get_object_or_404(Gallery, slug__iexact = 'main_page')
        g = gallery.latest(limit=3, public=True)
        context = {
                'isAbitu': True,
        #        'newsList': newsList,
		'decan': decan,
                'projectsList': projectsList,
                'gallery': g,
                'memorandum': memorandum
        }
        context.update(getDefaultContext(request))
        return render(request, 'main/base_abitur.html', context)

def about_decan(request):
	info = About_Decan.objects.all().first
	context = {
		'isDecan': True,
		'about':info
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_about_decan.html', context)

def LK(request):
	context = {}
	return render(request, 'main/base_LK.html', context)

def decan_time(request):
        #newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
        #projectsList = Projects.objects.filter(isFavorite = True)[:10]
        #memorandum = get_object_or_404(Articles, short_name__iexact = 'memorandum')
        #gallery = get_object_or_404(Gallery, slug__iexact = 'main_page')
        #g = gallery.latest(limit=3, public=True)
        decan = decanTime.objects.all()
	context = {
                'isDecan': True,
		'decans' : decan
                #'newsList': newsList,
                #'projectsList': projectsList,
                #'gallery': g,
                #'memorandum': memorandum
        }
        context.update(getDefaultContext(request))
        return render(request, 'main/base_decanTimetable.html', context)

def publication(request):
        #newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
        #projectsList = Projects.objects.filter(isFavorite = True)[:10]
        #memorandum = get_object_or_404(Articles, short_name__iexact = 'memorandum')
        publication = Publication.objects.order_by('-pub_date')[:10]
	#gallery = get_object_or_404(Gallery, slug__iexact = 'main_page')
        #g = gallery.latest(limit=3, public=True)
        context = {
                'isLib': True,
        #        'newsList': newsList,
		'publication':publication,
                #'projectsList': projectsList,
                #'gallery': g,
                #'memorandum': memorandum
        }
        context.update(getDefaultContext(request))
        return render(request, 'main/base_publication.html', context)

def facultat(request):        
	units = Units.objects.all()
	newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
        projectsList = Projects.objects.filter(isFavorite = True)[:10]
        memorandum = get_object_or_404(Articles, short_name__iexact = 'memorandum')
        gallery = get_object_or_404(Gallery, slug__iexact = 'main_page')
        g = gallery.latest(limit=3, public=True)
        context = {
                'units': units,
		'isIndex': True,
                'newsList': newsList,
                'projectsList': projectsList,
                'gallery': g,
                'memorandum': memorandum
        }
        context.update(getDefaultContext(request))
        return render(request, 'main/base_facultat.html', context)

def didjest_theme(request):
	theme = Didjest_theme.objects.all()
	context = {
		'isLib':True,
		'theme': theme
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_theme2.html', context)

def article(request, article):
	article = get_object_or_404(Articles, short_name = article)
	context = {
		'isArticle': True,
		'article': article
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/' + article.template, context)

def articleList(request):
	articlesList = Articles.objects.all().order_by('pub_date')[:10]
	context = {
		'isArticleList': True,
		'articlesList': articlesList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_articlList.html', context)

def department(request, department):
	cur_department = get_object_or_404(Departments, short_name = department)
	projectsList = cur_department.projects_set.all()[:5]
	articlesList = cur_department.article.filter(isFavorite = True).order_by('-pub_date')[:5]
	context = {
		'idDepartment': True,
		'department': cur_department,
		'projectsList': projectsList,
		'articlesList': articlesList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/' + cur_department.template, context)

def project(request, project):
	project = get_object_or_404(Projects, short_name = project)
	context = {
		'isProject': True,
		'project': project
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/' + project.template, context)

def projectList(request):
	projectsList = Projects.objects.all()[:10]
	context = {
		'isProjectList': True,
		'projectsList': projectsList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_projectList.html', context)

def news(request, news_id):
	news = get_object_or_404(News, pk = news_id)
	context = {
		'isLib': True,
		'news': news
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_news.html', context)

def didjest_list(request, id):
        didjest = get_object_or_404(Didjest_year, pk = id)
        didjest_list = didjest.didjest_set.all().order_by('-number')
        context = {
                'isLib': True,
                'didjests': didjest_list
        }
        context.update(getDefaultContext(request))
        return render(request, 'main/base_didjests.html', context)

def didjest_year(request, id):
        didjest = get_object_or_404(Didjest_theme, pk = id)
	didjest_list = didjest.didjest_year_set.all().order_by('-year')
        context = {
                'isLib': True,
                'didjest_year': didjest_list
        }
        context.update(getDefaultContext(request))
        return render(request, 'main/base_archive.html', context)

def newsList(request):
	newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
	context = {
		'isLib': True,
		'newsList': newsList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_newsList.html', context)

def bmstu(request):
	bmstu = AboutBMSTU.objects.get()
	context = {
		'isBmstu': True,
		'bmstu': bmstu
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_bmstu.html', context)

def contacts(request):
	context = {
		'isContacts': True
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_contacts.html', context)

def getDefaultContext(request):
	bannersList = Banners.objects.all()
	contacts = Contacts.objects.get()
	departmentsList = Departments.objects.all()
	context = {
		'location': request.path,
		'departmentsList': departmentsList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return context

















