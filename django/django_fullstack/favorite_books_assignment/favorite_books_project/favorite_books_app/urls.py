from django.urls import path
from . import views
urlpatterns = [
    path('',views.root),
    path('user_processing', views.processing),
    path('success',views.success),
    path('logout', views.logout),
    path('add_book',views.add_book),
    path('book_details/<id>',views.book_details),
    path('unfavorite/<id>', views.unfavorite),
    path('add_to_favorite/<id>',views.add_to_favorite),
    path('update/<id>',views.update),
    path('delete/<id>',views.delete),
]