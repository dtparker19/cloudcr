# cloudcr/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from cloudcr import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
