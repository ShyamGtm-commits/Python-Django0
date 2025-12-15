from django.urls import path
from .import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list.as_view(), name='task_list'),
    path('detail/<int:pk>/', views.task_detail.as_view(), name='task_detail'),
    path('banner/<int:pk>/', views.BannerPageView.as_view(), name='banner_view'),
    path('task_new/', views.task_new, name="task_new"),
    path('create/', views.task_create.as_view(), name='task_create'),
    path('update/<int:pk>/', views.task_update.as_view(), name='task_update'),
    path('delete/<int:pk>/', views.task_delete.as_view(), name='task_delete'),
]
