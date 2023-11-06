from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.my_requests_home, name='my_books_request'),
    path('<int:book_id>/<int:user_id>/accept', views.request_accept, name='request_accept'),
    path('<int:book_id>/<int:user_id>/deny', views.request_deny, name='request_deny'),
    path('<int:book_id>/withdraw', views.withdraw_book, name='withdraw_book'),
    path('<int:book_id>/<int:user_id>/accept_return', views.return_accept, name='return_accept'),
]
