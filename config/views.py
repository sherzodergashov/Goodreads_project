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
    return render(request, 'index.html')
