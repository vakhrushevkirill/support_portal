from django.urls import path
from . import views
from django.conf.urls import url
from .views import NewsList, NewsDetailView


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^news/$', NewsList.as_view(), name='news'),
    path('', views.index, name='index'),
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/add/', views.add_news, name='add_news'),

]