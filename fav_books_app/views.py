from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def logout(request):
    request.session.flush()
    return redirect('/')

def user(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session["user_id"])

    context = {
        "user": user,
        "uploaded_books": Book.objects.filter(uploaded_by = user),
        "favorited_books": Book.objects.filter(users_who_like = user),
        "all_other_books": Book.objects.exclude(users_who_like = user)
    }

    return render(request, 'user.html', context)

def add_book(request):
    return render(request, "add_book.html")

def create_book(request):
    if request.method == "POST":
    
        errors = Book.objects.validator(request.POST)

        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/books/add')

        user = User.objects.get(id=request.session["user_id"])
        new_book = Book.objects.create(title=request.POST['title'], desc = request.POST['desc'], uploaded_by=user)
        user.favorited_books.add(new_book)
        
        return redirect('/books')
    return redirect('books/add')

def view_book(request, id):
    this_book = Book.objects.get(id=id)

    context = {
        "this_book" : this_book,
        "user": User.objects.get(id=request.session["user_id"]),
        "users_who_like": this_book.users_who_like.all()
    }

    return render(request, "view_book.html", context)

def edit_book(request, id):
    this_book = Book.objects.get(id=id)

    context = {
        "user": User.objects.get(id=request.session["user_id"]),
        "this_book": Book.objects.get(id=id),
        "users_who_like": this_book.users_who_like.all()
    }

    return render(request, "edit_book.html", context)

def update(request, id):
    if request.method=="POST":
        errors = Book.objects.validator(request.POST)

        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(f'/books/{id}/edit')

        this_book=Book.objects.get(id=id)

        this_book.title = request.POST['title']
        this_book.desc = request.POST['desc']
        this_book.save()

    return redirect(f"/books/{id}")

def delete_book(request, id):
    if request.method == "POST":
        
        this_book=Book.objects.get(id=id)
        this_book.delete()

    return redirect('/books')

def add_fav(request, id):
    this_book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])

    user.favorited_books.add(this_book)

    return redirect('/books')

def remove_fav(request, id):
    this_book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])

    user.favorited_books.remove(this_book)

    return redirect('/books')

def add_fav_view(request, id):
    this_book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])

    user.favorited_books.add(this_book)

    return redirect(f'/books/{id}')

def remove_fav_view(request, id):
    this_book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])

    user.favorited_books.remove(this_book)

    return redirect(f'/books/{id}')