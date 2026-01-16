from django.shortcuts import render
from .models import blog

# Create your views here.

def BlogsView(request):
    blogs = blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blog})

