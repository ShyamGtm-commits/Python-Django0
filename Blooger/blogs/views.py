from django.shortcuts import render
from .models import blog
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class blogListView(ListView):
    model = blog
    template_name = "blog_list.html"

class blogCreateView(CreateView):
    model = blog
    fields = "__all__"
    success_url = reverse_lazy("blog_list")
    template_name = "blog_form.html"

class blogUpdateView(UpdateView):
    model = blog
    fields = "__all__"
    success_url = reverse_lazy("blog_list")
    template_name = "blog_form.html"

class blogDeleteView(DeleteView):
    model = blog
    success_url = reverse_lazy("blog_list")
    template_name = "blog_confirm_delete.html"