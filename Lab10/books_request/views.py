from django.shortcuts import redirect, render
from .models import Books_request
from database.models import Articles
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

@login_required
def my_requests_home(request):
    real_articles = []
    if request.user.is_staff:
        my_books = Books_request.objects.all()
    else:
        my_books = Books_request.objects.filter(user=request.user)
        for book in my_books:
            #print(book.status)
            try:
                if book.status == 'Approved':
                    article = Articles.objects.get(id=book.book_id)
                    real_articles.append(article)
            except:
                print('None. Error! books_request/views/my_requests_home')

    return render(request, 'books_request/my_requests_home.html',
                  {'my_books': my_books, 'real_articles': real_articles})


@login_required
def request_accept(request, book_id, user_id):
    Books_request.objects.filter(book_id=book_id, user_id=user_id).update(
        status='Approved',
        date_checked_by_admin=now()
    )
    # Получаем книгу по ID и убеждаемся, что она существует
    book = Articles.objects.get(id=book_id)
    book.quantity -= 1
    book.save(update_fields=['quantity'])
    return redirect('my_books_request')


@login_required
def request_deny(request, book_id, user_id):
    Books_request.objects.filter(book_id=book_id, user_id=user_id).update(
        status='Denied',
        date_checked_by_admin=now()
    )
    return redirect('my_books_request')


@login_required
def withdraw_book(request, book_id):
    Books_request.objects.filter(book_id=book_id, user_id=request.user.id).update(
        status='Returned',
        date_withdrawal=now()
    )
    return redirect('my_books_request')


@login_required
def return_accept(request, book_id, user_id):
    # Получаем книгу по ID и убеждаемся, что она существует
    book = Articles.objects.get(id=book_id)
    book.quantity += 1
    book.save(update_fields=['quantity'])
    #удаляем запись из бд
    Books_request.objects.filter(user_id=user_id, book_id=book_id).delete()
    return redirect('my_books_request')
