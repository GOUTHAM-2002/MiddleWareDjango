from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .forms import BookForm
from .models import Book
# Create your views here.

def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('index')

def index(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            form = BookForm()
            return redirect('index')
    else:
        form = BookForm()
    books=Book.objects.all()
    return render(request,'index.html',{'form':form,'books':books})

