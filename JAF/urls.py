from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('introduction.urls')),
    url(r'education', include('education.urls')),
    url(r'work', include('work.urls')),
    url(r'reference', include('reference.urls')),
    url(r'^admin/', admin.site.urls),
]
