from django.urls import path
from .import views

urlpatterns = [
    path('', views.book_list.as_view(), name ='book_list'),
    path('create/', views.book_create.as_view() ,name ='book_create'),
    path('update/<int:pk>/', views.book_update.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.book_delete.as_view(), name='book_delete'),
]