from django.shortcuts import render, redirect
from .models import blog
from .forms import blogForm

# Create your views here.


def BlogsView(request):
    blogs = blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def BlogsCreate(request):
    if request.method == "POST":
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        
    else:
        form = blogForm
    
    return render(request, 'blog_form.html', {'form': form})
        