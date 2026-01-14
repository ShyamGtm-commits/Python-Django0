from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blogListView.as_view(), name ='blog_list'),
    path('create/', views.blogCreateView.as_view(), name = 'blog_create'),
    path('update/<int:pk>/', views.blogUpdateView.as_view(), name = 'blog_update'),
    path('delete/<int:pk>/', views.blogDeleteView.as_view(), name = 'blog_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)