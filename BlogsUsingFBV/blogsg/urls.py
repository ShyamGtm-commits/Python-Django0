from django.urls import path
from .import views

urlpatterns = [
    path('', views.BlogsView, name='blog_list'),
    path('blogs_create/', views.BlogsCreate, name='blog_create'),
    path('blogs_update/<int:pk>/', views.BlogsUpdate, name='blog_update'),

]
