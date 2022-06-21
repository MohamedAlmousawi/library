
from .forms import *
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    if request.method == "POST":
        books_add = BookForm(request.POST,request.FILES)
        if books_add.is_valid():
            books_add.save()
            return redirect('/')
        category_add = CategoryForm(request.POST,request.FILES)
        if category_add.is_valid():
            category_add.save()
            return redirect('/')

    NumberOfBooks = Book.objects.all().count()
    category1=Category.objects.all()
    books =Book.objects.all()
    bookform =BookForm() 
    categoryform = CategoryForm()
    tuple = {'NumberOfBooks':NumberOfBooks,'books':books,"category1":category1,'bookform':bookform,'categoryform':categoryform}
    
    return render(request,'pages/home.html',tuple)

def books(request):
    books = Book.objects.all()
    if 'search_name' in request.GET :
        search_title = request.GET.get('search_name')
        if search_title:
            books = Book.objects.filter(title__icontains=search_title)
    tuple = {'books':books}
    return render(request,'pages/books.html',tuple)