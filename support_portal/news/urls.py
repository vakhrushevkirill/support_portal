from django.urls import path
from . import views
from django.conf.urls import url
from .views import NewsList, NewsDetailView


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^news/$', NewsList.as_view(), name='news'),
    path('', views.index, name='index'),
    path('list/', NewsList.as_view(), name='news_list'),
    path('list/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add/', views.add_news, name='add_news'),

]