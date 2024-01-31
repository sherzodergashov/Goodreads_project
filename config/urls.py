from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home_page, book_list, book_random

urlpatterns = [
    path("book_list/", book_list, name='book_list'),
    path("home/", home_page, name='home_pages'),
    path("", book_random, name='helloworld'),
    path("users/", include("users.urls")),
    path("books/", include("books.urls")),
    path("API/", include("API.urls")),


    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
