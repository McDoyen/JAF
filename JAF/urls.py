from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'introduction', include('introduction.urls')),
    url(r'', include('education.urls')),
    url(r'^admin/', admin.site.urls),
]
