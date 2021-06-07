from django.conf.urls import url
from mongo import views
from django.urls import include

urlpatterns = [
    url(r'^getWebSite/$', views.getOrganizationName.as_view()),
    url(r'^getColumn/$', views.getCollegeName.as_view()),
]
