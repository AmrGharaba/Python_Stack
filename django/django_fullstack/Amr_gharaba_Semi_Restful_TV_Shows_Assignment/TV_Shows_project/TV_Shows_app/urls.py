from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.root),
    path('shows/tv_form',views.tv_form),
    path('shows/tv_add',views.tv_add),
    path('shows/<id>', views.show_detail),
    path('shows/delete/<id>', views.delete),
    path('shows/edit/<id>', views.edit_form),
    path('shows/update/<id>', views.update),
]