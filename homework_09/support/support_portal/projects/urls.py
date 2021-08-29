from django.urls import path
from . import views
from django.conf.urls import url
from .views import MembersList, ProjectsList, TasksList, TaskDetailView


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^news/$', NewsList.as_view(), name='news'),
    path('members/', MembersList.as_view(), name='members_list'),
    path('members/<int:pk>/', ProjectsList.as_view(), name='projects_list'),
    path('members/<int:pk1>/<int:pk2>/', TasksList.as_view(), name='tasks_list'),
    path('members/<int:member_pk>/<int:project_pk>/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('members/<int:pk1>/<int:pk2>/create_task/', views.create_task, name='create_task')
]