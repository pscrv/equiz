from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^question/(?P<pk>\d+)/(?P<clicked>\d+)$', views.question_page, name='question'),
    url(r'^question/(?P<pk>\d+)/$', views.question_page, name='question')
]
