from django.contrib import admin
from books.models import Book, Auther, BookAuthor, BookReview, Type, Order


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn', 'type')
    list_filter = ['type']
    list_display = ('title', 'isbn', 'description')


class AutherAdmin(admin.ModelAdmin):
    search_fields = ('last_name', 'first_name')
    list_display = ('last_name', 'first_name', 'email', 'bio')


class BookAutherAdmin(admin.ModelAdmin):
    pass


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'stars_given', 'created_at']
    readonly_fields = ['created_at', ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'count', 'date')

class TypeAdmin(admin.ModelAdmin):
    list_filter = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Auther, AutherAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(BookAuthor, BookAutherAdmin)
admin.site.register(BookReview, BookReviewAdmin)
