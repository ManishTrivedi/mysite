"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello
from books import views
from books.views import PublisherList
from books.views import BookList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^search/$', views.search),
    url(r'^publisher/$', PublisherList.as_view()),
    url(r'^publisher-api/$', views.PublisherListAPI.as_view()),
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
    url(r'^booklist/$', views.BookList.as_view()),
    url(r'^', include(router.urls)),
]
