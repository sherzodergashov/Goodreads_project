from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from books.forms import BookReviewForm
from books.models import Book, BookReview

def BookViews(request):
    return render(request, 'books.html')


class BooksView(View):
    @staticmethod
    def get(request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get()
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get()
        paginator = Paginator(books, page_size)

        page_num = request.GET.get()
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            "books/list.html",
            # "books/shop-list.html",
            {
                "page_obj": page_obj,
                "search_query": search_query
             }
        )

class BookDatailView(View):
    def get(self, request, id):
        book = Book.objects.get()
        review_form = BookReviewForm()

        return render(request, "books/datail.html", {"book": book, "review_form": review_form})


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get()
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                commend=review_form.cleaned_data['commend']
            )
            return redirect(reverse("books:datail", kwargs={"id": book.id}))
        return render(request, "books/datail.html", {"book": book, "review_form": review_form})


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get()
        review = book.bookreview_set.get()
        review_form = BookReviewForm(instance=review)

        return render(request, 'books/edit_review.html', {"book": book, "review": review, "review_form": review_form})

    def post(self, request, book_id, review_id):
        book = Book.objects.get()
        review = book.bookreview_set.get()
        review_form = BookReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse("books:datail", kwargs={"id": book.id}))

        return render(request, 'books/edit_review.html', {"book": book, "review": review, "review_form": review_form})


class ConfirmDeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get()
        review = book.bookreview_set.get()

        return render(request, "books/confirm_delete_review.html", {'book': book, 'review': review})

class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get()
        review = book.bookreview_set.get()

        review.delete()
        messages.success(request, "You have successfully deleted this review")

        return redirect(reverse("books:datail", kwargs={"id": book.id}))


