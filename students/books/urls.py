from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^books/$', views.book_list),
]

