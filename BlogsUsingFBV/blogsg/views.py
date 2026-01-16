from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from .forms import blogForm

# Create your views here.


def BlogsView(request):
    blogs = blog.objects.all().order_by('date_created')
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


def BlogsUpdate(request, pk):
    blog_instance = get_object_or_404(blog, pk=pk)

    if request.method == "POST":
        form = blogForm(request.POST or None, request.FILES,
                        instance=blog_instance)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = blogForm(instance=blog_instance)

    return render(request, 'blog_form.html', {'form': form})


def BlogDelete(request, pk):
    blog_instance = get_object_or_404(blog, pk=pk)

    if request.method == "POST":
        blog_instance.delete()
        return redirect('blog_list')

    return render(request, 'blog_confirm_delete.html', {'blog': blog_instance})
