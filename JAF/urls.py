from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('forms.urls')),
    path('admin/', admin.site.urls),
]
