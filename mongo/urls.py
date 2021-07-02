from django.conf.urls import url
from mongo import views
from django.urls import include

urlpatterns = [
    url(r'^getWebSite/$', views.getOrganizationName.as_view()),
    url(r'^getColumn/$', views.getCollegeName.as_view()),
    url(r'^addStrategy/$', views.addStrategy.as_view()),
    url(r'^xpathManage/$', views.xpathManage.as_view()),
    url(r'^manageSpecXpath/$', views.manageSpecXpath.as_view()),
    url(r'^crawlerLog/$', views.crawlerLog.as_view()),
    url(r'^crawlerSpecLog/$', views.crawlerSpecLog.as_view()),
]
