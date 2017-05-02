
from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [

    url(r'^login/$', views.login , name='login'),
    url(r'^register/$', views.register , name='register'),
    url(r'^plogin', views.loginp , name='loginp'),
    url(r'^pregister', views.registerp , name='registerp'),
    url(r'^admin/t$', views.index , name='index'),
    url(r'^add/t$', views.trainCreate.as_view() , name='productadd'),
    url(( r'^(?P<pk>[0-9]+)/t$'), views.DetailView.as_view(), name='detailt'),

    url(r'^(?P<pk>[0-9]+)/updatet/$', views.trainUpdate.as_view() , name='updatet'),

    url(r'^(?P<pk>[0-9]+)/deletet/$', views.trainDelete.as_view() , name='deletet'),
      #url(r'',views.error , name='all_store'),
    url(r'^add/s$', views.stCreate.as_view() , name='productadd'),
    url(( r'^(?P<pk>[0-9]+)/s$'), views.stView.as_view(), name='detail'),

    url(r'^(?P<pk>[0-9]+)/updates/$', views.stUpdate.as_view() , name='productup'),

    url(r'^(?P<pk>[0-9]+)/deletes/$', views.stDelete.as_view() , name='productdel'),

    url(r'^add/d$', views.dCreate.as_view() , name='productadd'),
    url(( r'^(?P<pk>[0-9]+)/d$'), views.dView.as_view(), name='detail'),

    url(r'^(?P<pk>[0-9]+)/updated/$', views.dUpdate.as_view() , name='productup'),

    url(r'^(?P<pk>[0-9]+)/deleted/$', views.dDelete.as_view() , name='productdel'),
    url(( r'^search/t$'), views.searcht, name='detailt'),

    url(( r'^search/tp$'), views.searchtp, name='detailt'),
    url(( r'^search/sp$'), views.searchsp, name='detailt'),
    url(( r'^search/s$'), views.searchs, name='detailt'),
    url(( r'^search/bws$'), views.bws, name='detailt'),
    url(( r'^search/bwsp$'), views.bwsProcess, name='detailt'),
    url(( r'^admin/(?P<pk>[0-9]+)$'), views.trainDetail, name='detailt'),
]
