from django.urls import path

from . import views

urlpatterns = [
    path('', views.introduction, name='index'),
    path('education/', views.education, name='education'),
    path('work/', views.work, name='work'),
    path('reference/', views.reference, name='reference'),
]
