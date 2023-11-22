from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('quest',views.quest),
    path('reset', views.reset)
]