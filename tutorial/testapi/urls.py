from django.conf.urls import url
from testapi import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^student_index', views.student_index),
]
