from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.introduction, name='index'),
    url(r'^education/$', views.education, name='education'),
    url(r'^work/$', views.work, name='work'),
    url(r'^reference/$', views.reference, name='reference'),
]
