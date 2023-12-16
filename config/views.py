from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

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

# def index_view(request):
#     books = Book.objects.all().order_by('id')
#     search_query = request.GET.get("q", "")
#     if search_query:
#         books = books.filter(title__icontains=search_query)
#
#     page_size = request.GET.get("page_size", 7)
#     paginator = Paginator(books, page_size)
#
#     page_num = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_num)
#
#     return render(
#         request,
#         "index.html",
#         {
#             "page_obj": page_obj,
#             "search_query": search_query
#          }
#     )

class BooksIndex(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'index.html'

    def get_queryset(self):
        most_view = Book.objects.order_by('?')
        new_arrival = Book.objects.all().order_by('id')
        return most_view
def ProductDetails(request):
    return render(request, 'product-details.html')

def ShopGrid(request):
    return render(request, 'shop-grid.html')

def ShopList(request):
    return render(request, 'shop-list.html')
