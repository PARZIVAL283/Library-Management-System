from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

#Book model to represent a book in the library
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

#Issue book model
class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    
    def calculate_fine(self):
        if self.return_date:
            days = (self.return_date - self.issue_date).days
        else:
            from django.utils import timezone
            days = (timezone.now() - self.issue_date).days

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"