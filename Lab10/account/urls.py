from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
 #   path('logout/', views.sign_out, name='logout'),
    path('main/', include('main.urls')),
    path('database/', include('database.urls')),
    path('my_books_request/', include('books_request.urls')),
    path('register/', views.sign_up, name='register'),
 ]

