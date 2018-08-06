from . import views
from django.conf.urls import url, include

urlpatterns = [
    url('^$', views.template, name = 'Template'),
    url('^contact/$', views.contact, name = 'Template'),
]