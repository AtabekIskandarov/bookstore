from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def homepage(request):
    return render(request, "bookstore.html")


def add_todo(request):
    form = request.POST
    text = form["bookstore_bookstore"]
    todo = ToDo(bookstore=text)
    todo.save()
    return redirect(bookstore)


