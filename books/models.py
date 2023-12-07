from django.utils import timezone
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    cover_picture = models.ImageField(default="default_cover.jpg")
    # narxi = models.DecimalField(max_length=10, decimal_places=2)
    # tili = models.

    def __str__(self):
        return str(self.title)

class Auther(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} by {self.auther.last_name} {self.auther.first_name}"


class BookReview(models.Model):
    objects = None
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    commend = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.stars_given} stars for {self.book.title} by {self.user.username}"

