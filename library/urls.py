from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('issue/<int:book_id>/', views.issue_book, name='issue_book'),
    path('return/<int:issue_id>/', views.return_book, name='return_book'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]