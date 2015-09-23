from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	#Articles
	url(r'^article/all/$', views.articleList, name='articleList'),
    url(r'^article/(?P<article>\w+)/$', views.article, name='article'),
        #facultat
	url(r'^facultat/$', views.facultat, name='facultat'),
    #Projects
    url(r'^project/all/$', views.projectList, name='projectList'),
	url(r'^project/(?P<project>\w+)/$', views.project, name='project'),
	#Didjest_theme
    url(r'^Didjest_theme/$', views.didjest_theme, name='Didjest_theme'),
    	#Didjest_year
    url(r'^Didjest_theme/(?P<id>\d+)/$', views.didjest_year, name='Didjest_year'),
	#didjest_list
    url(r'^didjest_list/(?P<id>\d+)/$', views.didjest_list, name='Didjest_list'),
	#about_decan
    url(r'^about_decan/$', views.about_decan, name='about_decan'),
	#decan_time
    url(r'^decantime/$', views.decan_time, name='decan_time'),
	#about_decan
    url(r'^LK/$', views.LK, name='LK'),
	#Departments
    url(r'^department/(?P<department>\w+)/$', views.department, name='department'),
	
	#abitur
    url(r'^abitu/$', views.abitu, name='abitu'),

	#publication
    url(r'^publication/$', views.publication, name='publication'),

    #News
    url(r'^news/all/$', views.newsList, name='newsList'),
	url(r'^news/(?P<news_id>\d+)/$', views.news, name='news'),

	#bmstu
	url(r'^bmstu/$', views.bmstu, name='bmstu'),

	#contacts
	url(r'^contacts/$', views.contacts, name='contacts'),
)
