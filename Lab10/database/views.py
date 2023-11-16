from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



def staff_check(user):
    return user.is_authenticated and user.is_staff


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


def database_home(request):
    databases = Articles.objects.all()
    return render(request, 'database/database_home.html', {'databases': databases})



class BooksDetailView(DetailView):
    model = Articles
    template_name = 'database/details_view.html'
    context_object_name = 'article'


class BooksUpdateView(StaffRequiredMixin, UpdateView):
    model = Articles
    template_name = 'database/create.html'
    form_class = ArticlesForm


class BooksDeleteView(StaffRequiredMixin, DeleteView):
    model = Articles
    success_url = '/database'
    template_name = 'database/books-delete.html'


@login_required
def ask_for_the_books(request, article_id):
    if request.method == 'POST':
        action = request.POST.get("action")
        if action == "assign":
            users = User.objects.all()  # Получаем всех пользователей
            return render(request, 'database/assign_book.html', {'users': users, 'book_id': article_id})
        elif action == "revoke":
            users_with_book = Articles.objects.filter(id=article_id, owner__isnull=False)  # Получаем всех пользователей
            return render(request, 'database/revoke_book.html', {'users_with_book': users_with_book, 'book_id': article_id})
        elif action[0] in '123456789':
            book = Articles.objects.get(id=article_id)
            user = User.objects.get(id=int(action))
            if book.owner == user:
                print('already')
            else:
                book.owner = user
                book.save()
                print(action)
                print(article_id)
                return redirect('home')
        elif action[0] in '0':
            action = action[1:]
            book = Articles.objects.get(id=article_id)
            book.owner = None
            book.save()
            print(action)
            print(article_id)
            return redirect('home')
        created = None
        if created:
            # Если запись была создана, отправляем пользователя обратно на страницу книг с сообщением
           # print("Book added to your collection.")
            print("Request!")
           # books_request.save()
        else:
            # Если запись уже существует, сообщаем об этом пользователю
           # print("You already have this book in your collection.")
            print("You have already tried!")
        return database_home(request)


@user_passes_test(staff_check)
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'


    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'database/create.html', data)


class SearchResultsView(ListView):
    model = Articles
    template_name = 'database/database_home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Articles.objects.filter(
                Q(title__icontains=query) |
                Q(anons__icontains=query) |
                Q(autor__icontains=query),
                quantity__gt=0
            ).distinct()  # использование distinct() для избежания дубликатов
        return Articles.objects.none()