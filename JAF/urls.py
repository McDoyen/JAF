from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'introduction', include('introduction.urls')),
    url(r'education', include('education.urls')),
    url(r'', include('work.urls')),
    url(r'^admin/', admin.site.urls),
]
