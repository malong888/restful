from django.conf.urls import url
from testapi import views

urlpatterns = [
    url(r'^book_index/$', views.book_index),
]

