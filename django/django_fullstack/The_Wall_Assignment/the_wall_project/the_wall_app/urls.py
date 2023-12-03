from django.urls import path
from . import views
urlpatterns = [
    path('',views.root),
    path('user_processing',views.user_processing),
    path('user_interface',views.user_interface),
    path('log_out',views.log_out),
    path('post_message',views.post_message),
    path('add_comment/<id>',views.add_comment),
    path('delete/<id>',views.delete_message)
]