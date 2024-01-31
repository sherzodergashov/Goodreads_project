from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from books.models import BookReview, Book, Type
from books.views import BooksView
from django.core.mail import send_mail

def Hello(request):
    return render(request, 'Hello.html')
def home_page(request):
    type_book = Type.objects.all()
    book_reviews = BookReview.objects.all().order_by("-created_at")
    book_size = request.GET.get("page_size", 10)
    paginator = Paginator(book_reviews, book_size)

    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)

    return render(request, "home.html", {"page_obj": page_object, 'book_type': type_book})

def book_list(request):
    books = Book.objects.all()

    return render(request, "book_list.html", {"book_review": books})


def book_random(request):
    type_book = Type.objects.all()
    book_all = Book.objects.all()
    books = Book.objects.all().order_by('?')
    book_size = request.GET.get('page_size', 40)
    paginator = Paginator(books, book_size)

    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)

    context = {
        'book_list': page_object,
        'book_all': book_all,
        'book_type': type_book
    }

    # //////////////////////
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'email': email,
            'message': message
        }
        message = ''' 
        New message: {}
        
        Form: {}
        '''.format(data['message'], data['email'])
        send_mail(data['email'], message, '', ['sherzod.ergashov.4501@gmail.com'])
    return render(request, 'Hello.html', context)
