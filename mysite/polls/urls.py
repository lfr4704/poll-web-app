


from . import views
from django.urls import include, path
#solution from https://spapas.github.io/2015/04/29/django-show-404-page/
import django.views.defaults

urlpatterns = [
    path('test/', views.index)
]
