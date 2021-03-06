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
    url(r'^getXpathByColumn/$', views.getXpathByColumn.as_view()),
    url(r'^getXpathByName/$', views.getXpathByName.as_view()),
    url(r'^getXpathValueNameList/$', views.getXpathValueNameList.as_view()),
    url(r'^getCrawlerStrategyLs/$', views.getCrawlerStrategyLs.as_view()),
    url(r'^modifyOneSpecXpath/$', views.modifyOneSpecXpath.as_view()),
    url(r'^modifyLog/$', views.modifyLog.as_view()),
    url(r'^getAllXpathValueNameList/$', views.getAllXpathValueNameList.as_view()),
    url(r'^addXpathByFile/$', views.uploadXpathByFile.as_view()),
    url(r'^getManyXpath/$', views.getXpathByQuery.as_view()),
]

# url(r'^uploadXpathByFile/$', views.uploadXpathByFile.as_view()), 这样是错的
