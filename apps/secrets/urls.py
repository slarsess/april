from django.conf.urls import url
# from django.contrib import admin

from . import views
app_name ='secrets'
urlpatterns = [
    url(r'^recent$', views.recent, name ='recent'),
    url(r'^post$', views.post, name='post'),
    url(r'^popular$', views.popular, name='popular'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
]
