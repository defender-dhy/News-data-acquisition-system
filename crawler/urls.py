from django.conf.urls import url
from crawler import views
from django.urls import include

urlpatterns = [
    url(r'^wechatCrawler/$', views.wechatCrawler.as_view()),
    url(r'^newsCrawler/$', views.newsCrawlerOne.as_view()),
    url(r'^newsCrawlerAll/$', views.newsCrawlerAll.as_view()),
    url(r'^getProcess/$', views.newsCrawlerAll.as_view()),
    url(r'^newsCrawlerOne/$', views.newsCrawlerOne.as_view())
]
