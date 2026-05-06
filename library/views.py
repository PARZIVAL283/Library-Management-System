# Views for the library system
from django.shortcuts import render, redirect
from .models import Book, Issue
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def home(request):
    return render(request, 'home.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


@login_required
def issue_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if book.available:
        Issue.objects.create(user=request.user, book=book)
        book.available = False
        book.save()

    return redirect('book_list')


@login_required
def return_book(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.return_date = timezone.now()
    issue.book.available = True
    issue.book.save()
    issue.save()

    return redirect('book_list')


from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    issues = Issue.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'issues': issues})

def book_list(request):
    query = request.GET.get('q')
    
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'books.html', {'books': books})

from django.core.paginator import Paginator

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books.html', {'page_obj': page_obj})