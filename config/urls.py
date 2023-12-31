"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from books.views import BookViews
from .views import home_page, book_list, Hello, ShopList, ShopGrid, ProductDetails, book_random

urlpatterns = [
    path("book_list/", book_list, name='book_list'),
    path("home/", home_page, name='home_pages'),
    path("rasm/", BookViews, name="books_kitoblar"),
    path("", book_random, name='helloworld'),
    path("users/", include("users.urls")),
    path("books/", include("books.urls")),
    path("API/", include("API.urls")),


    # path("index/", index_view, name="index"),
    # path("index/", BooksIndex.as_view(), name="index"),
    path("shop-list/", ShopList, name='shop-list'),
    path("shop-grid/", ShopGrid, name='shop-grid'),
    path("product-details/", ProductDetails, name='product-details'),


    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
