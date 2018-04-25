


from django.contrib import admin
from django.urls import include, path
#solution from https://spapas.github.io/2015/04/29/django-show-404-page/
import django.views.defaults

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #
    url(r'^404/$', django.views.defaults.page_not_found, ),
]
