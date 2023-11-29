from django.urls import path
from . import views
urlpatterns = [
    path('',views.root),
    path('user_processing', views.processing),
    path('success',views.success),
    path('logout', views.logout),
]