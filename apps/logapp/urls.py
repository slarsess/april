from django.conf.urls import url
from . import views

app_name = "logapp"
urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout')
    # url(r'^admin/', admin.site.urls),
]
