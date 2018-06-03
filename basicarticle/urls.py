"""article URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from basicarticle.views import *
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^article/$', csrf_exempt(Articles.as_view()), name='Articles'),
	url(r'^create/$', csrf_exempt(CreateArticle.as_view()), name='CreateArticle'),
	#url(r'^upvote/(?P<article_id>\d+)/$', csrf_exempt(UpvoteArticle.as_view()), name='UpvoteArticle'),
	url(r'^upvote/$', csrf_exempt(UpvoteArticle.as_view()), name='UpvoteArticle'),
]