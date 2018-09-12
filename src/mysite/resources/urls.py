# resources/urls.py
from django.conf.urls import url
from resources import views



urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]