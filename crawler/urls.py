from django.conf.urls import url
from crawler import  views
from django.urls import include

urlpatterns = [
    url(r'^wechatCrawler/$', views.wechatCrawler.as_view()),
    url(r'^newsCrawler/$', views.newsCrawler.as_view())
]
