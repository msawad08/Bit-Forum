from django.conf.urls import url

from forumapp import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

]
