from django.urls import path
from . import views

urlpatterns = [
    path('', views.database_home, name='database_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BooksDetailView.as_view(), name='books-detail'),
    path('<int:pk>/update', views.BooksUpdateView.as_view(), name='books-update'),
    path('<int:pk>/delete', views.BooksDeleteView.as_view(), name='books-delete'),
    path('my_books_request/<int:article_id>/', views.ask_for_the_books, name='my_books_request'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),

]