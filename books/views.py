from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from books.forms import BookReviewForm
from books.models import Book, BookReview, Type, Order
from users.models import CustomUser

def CategorieView(request):
    books = Book.objects.all()

    page_size = request.GET.get("page_size", 6)
    paginator = Paginator(books, page_size)

    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        "page_object": page_obj
    }

    return render(request, 'books/categories/categorie.html', context)

def BlogView(request):
    return render(request, 'blogs/book-blog.html')

def NewsView(request):
    return render(request, 'blogs/news.html')

def WishListView(request):
    return render(request, 'blogs/wishlist.html')

def CartView(request):
    return render(request, 'blogs/cart.html')


class BooksView(View):
    @staticmethod
    def get(request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get("q", "")
        if search_query:
            books = books.filter(title__icontains=search_query)

        page_size = request.GET.get("page_size", 7)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        type_book = Type.objects.all()
        book_review = BookReview.objects.all()
        # user = request.session['username']
        # customuser = CustomUser.objects.get(username=user)
        #
        # if request.method == "POST":
        #     stars_given = request.POST.get('star')
        #     messages = request.POST.get('message')
        #
        #     reviews = BookReview(user=customuser, book=books, stars_given=stars_given, review_message=messages)
        #     reviews.save()
        return render(
            request,
            "books/list.html",
            # "books/datail.html",
            {
                "b_review": book_review,
                "page_obj": page_obj,
                "search_query": search_query,
                'book_type': type_book
             }
        )

class BookDatailView(View):
    @staticmethod
    def get(request, id):
        type_book = Type.objects.all()
        # totalitem = 0
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        review_detail = BookReview.objects.filter(id=id)
        # item_already_in_cart = False
        # if request.user.is_authenticated:
        #     totalitem = len(Order.objects.filter(user=request.user))
        #     item_already_in_cart = Order.objects.filter(Q(book=book.id) & Q(user=request.user)).exists()

        return render(request, "books/datail.html", {
            "book": book,
            "review_form": review_form,
            'review_detail': review_detail,
            'book_type': type_book,
            # 'item_already_in_cart': item_already_in_cart,
            # 'totalitem': totalitem
        })

    # def post(self, request, id):
    #     book = Book.objects.get(id=id)
    #     review_form = BookReviewForm(request.POST)
    #     if review_form.is_valid():
    #         new_review = review_form.save(commit=False)
    #         new_review.book = book
    #         new_review.user = request.user
    #         new_review.save()
    #         return redirect('datail', id=id)
    #     else:
    #         totalitem = len(Order.objects.filter(user=request.user))
    #         item_already_in_cart = Order.objects.filter(
    #             Q(book=book.id) & Q(user=request.user)
    #         ).exists()
    #         reviews = BookReview.objects.filter(book=book)
    #         return render(request, "books/datail.html", {
    #             "book": book,
    #             "review_form": review_form,
    #             # 'review_detail': review_detail,
    #             'item_already_in_cart': item_already_in_cart,
    #             'totalitem': totalitem
    #         })



class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        type_book = Type.objects.all()
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                commend=review_form.cleaned_data['commend']
            )
            return redirect(reverse("books:datail", kwargs={"id": book.id}))
        return render(request, "books/datail.html", {
            "book": book,
            "review_form": review_form,
            'book_type': type_book
        })


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        type_book = Type.objects.all()
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)

        return render(request, 'books/edit_review.html', {
            "book": book,
            "review": review,
            "review_form": review_form,
            'book_type': type_book
        })

    def post(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review, data=request.POST)
        type_book = Type.objects.all()

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse("books:datail", kwargs={"id": book.id}))

        return render(request, 'books/edit_review.html', {
            "book": book, "review": review,
            "review_form": review_form,
            'book_type': type_book
        })


class ConfirmDeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        type_book = Type.objects.all()

        return render(request, "books/confirm_delete_review.html", {
            'book': book,
            'review': review,
            'book_type': type_book
        })

class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)

        review.delete()
        messages.success(request, "You have successfully deleted this review")

        return redirect(reverse("books:datail", kwargs={"id": book.id}))


