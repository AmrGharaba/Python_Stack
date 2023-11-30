from django.urls import path
from . import views
urlpatterns = [
    path('',views.root),
    path('user_processing', views.processing),
    path('success',views.success),
    path('logout', views.logout),
    path('add_book',views.add_book),
    path('book_details/<id>',views.book_details),
    path('unfavorite/<id>', views.unfavorite)
]