from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BookForm
from .models import Books

# Create your views here.

# we'll start simply by making a bookform
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Books
#         fields = ['title', 'author', 'description']

# now listing all the books

def book_list(request):
    books = Books.objects.all()
    return render(request, 'books/book_list.html',{'books': books})

# creating a new book
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request,'books/book_form.html',{'form': form})

# then to update a book
 
def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)

    form = BookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html',{'form': form })

# to delete a book

def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk)

    if request.method =="POST":
        book.delete()
        return redirect('book_list')
    return render(request,'books/book_confirm_delete.html',{'book': book})


    
        