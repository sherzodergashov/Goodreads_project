from rest_framework import serializers

from books.models import Book, BookReview
from users.models import CustomUser


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')
    # title = serializers.CharField(max_length=200)
    # description = serializers.CharField()
    # isbn = serializers.CharField(max_length=17)

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'username')
    # username = serializers.CharField(max_length=100)
    # first_name = serializers.CharField(max_length=50)
    # last_name = serializers.CharField(max_length=50)
    # email = serializers.EmailField()

class BookReviewSerializers(serializers.ModelSerializer):
    book = BookSerializers()
    user = UserSerializers()

    class Meta:
        model = BookReview
        fields = ('id', 'stars_given', 'commend', 'book', 'user')
    # stars_given = serializers.IntegerField(min_value=1, max_value=5)
    # commend = serializers.CharField()
    # book = BookSerializers()
    # user = UserSerializers()





