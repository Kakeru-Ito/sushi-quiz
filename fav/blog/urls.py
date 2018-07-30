from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url('output',views.output),
    url('more',views.more),
    url('post_list',views.post_list),
    url('result',views.result),
	url('first',views.post_list)
]
