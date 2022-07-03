from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('forms.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico")))
]
