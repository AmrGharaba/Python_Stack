from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('add_book',views.add_book),
    path('add_author',views.add_author),
    path('books/<id>', views.book_detail),
    path('authors/<id>', views.author_detail),
    path('add_book_author', views.add_book_author),
    path('add_author_book', views.add_author_book),



]