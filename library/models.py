from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.

def default_return_date():
    pass

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

class Membership(models.Model):
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=timezone.now() + timedelta(days=30))

    def __str__(self):
        return f"{self.book} - {self.membership}"
