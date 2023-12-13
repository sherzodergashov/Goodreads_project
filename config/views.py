from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from books.models import BookReview, Book
from books.views import BooksView

def Hello(request):
    return render(request, 'Hello.html')
def home_page(request):
    book_reviews = BookReview.objects.all().order_by("-created_at")
    book_size = request.GET.get("page_size", 10)
    paginator = Paginator(book_reviews, book_size)

    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)

    return render(request, "home.html", {"page_obj": page_object})

def book_list(request):
    books = Book.objects.all()

    return render(request, "book_list.html", {"book_review": books})

def index_html_view(request):
    books = Book.objects.all().order_by('id')
    book_size = request.GET.get('page_size', 12)
    paginator = Paginator(books, book_size)

    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)

    books = Book.objects.all().order_by('-id')
    book_size1 = request.GET.get('page_size', 12)
    paginator1 = Paginator(books, book_size1)

    page_num1 = request.GET.get('page', 1)
    page_object1 = paginator1.get_page(page_num1)
    context = {
        'book_list': page_object,
        'book_list2': page_object1
    }
    return render(request, 'index.html', context)

def ProductDetails(request):
    return render(request, 'product-details.html')

def ShopGrid(request):
    return render(request, 'shop-grid.html')

def ShopList(request):
    return render(request, 'shop-list.html')
