from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import BookReview, Order
from API.serializers import BookReviewSerializers, OrderSerializers


class BookReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)

        serializer = BookReviewSerializers(book_review)
        return Response(data=serializer.data)


class BookAPIReviewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_list = BookReview.objects.all().order_by('-created_at')

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_list, request)

        serializer = BookReviewSerializers(page_obj, many=True)
        return paginator.get_paginated_response(serializer.data)

class OrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        order = Order.objects.get(id=id)

        serializers = OrderSerializers(order)
        return Response(data=serializers.data)

class OrderViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders_book = Order.objects.all().order_by('id')

        serializer = OrderSerializers(orders_book, many=True)
        return Response(data=serializer.data)
