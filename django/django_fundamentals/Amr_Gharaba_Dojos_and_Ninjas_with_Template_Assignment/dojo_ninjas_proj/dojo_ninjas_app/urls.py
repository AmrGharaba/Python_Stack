from django.urls import path
from . import views
urlpatterns = [
    path('', views.root ),
    path('dojo', views.dojo),
    path('ninja', views.ninja),
    path('delete/<str:dojo>', views.delete),

]