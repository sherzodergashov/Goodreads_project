from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from books.models import BookReview, Book, Type
from books.views import BooksView

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
    # featured products
    type_book = Type.objects.all()
    # type_size = request.GET.get()
    # p = Paginator(type_book, type_size)
    books = Book.objects.all().order_by('?')
    book_size = request.GET.get('page_size', 16)
    paginator = Paginator(books, book_size)

    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)

    context = {
        'book_list': page_object,
        'book_type': type_book
    }
    return render(request, 'Hello.html', context)

def ProductDetails(request):
    return render(request, 'product-details.html')

def ShopGrid(request):
    return render(request, 'shop-grid.html')

def ShopList(request):
    return render(request, 'shop-list.html')
