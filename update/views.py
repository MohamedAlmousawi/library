from django.shortcuts import redirect, render
from home1.forms import BookForm

from home1.models import Book

# Create your views here.

def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        book_update = BookForm(request.POST,request.FILES,instance=book_id)
        if book_update.is_valid():
            book_update.save()
        return redirect('/')
    else:
        book_information = BookForm(instance=book_id)

    
    return render(request,'pages/update.html',{'bookform':book_information})