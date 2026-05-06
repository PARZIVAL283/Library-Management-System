from django.contrib import admin
from .models import Book, Issue

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available')
    search_fields = ('title', 'author')

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'issue_date', 'return_date')