from django.shortcuts import redirect, render

from home1.models import Book

# Create your views here.

def delete(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        book_id.delete()
        return redirect('/')
    return render(request,'pages/delete.html')