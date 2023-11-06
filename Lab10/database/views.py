from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse
from books_request.models import Books_request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



def staff_check(user):
    return user.is_authenticated and user.is_staff


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


def database_home(request):
    databases = Articles.objects.filter(quantity__gt=0)
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
        user = User.objects.get(id=request.user.id)
        article = Articles.objects.get(id=article_id)
        # Проверяем, существует ли уже такая запись
        books_request, created = Books_request.objects.get_or_create(
            user=user,
            book=article
        )
        if created:
            # Если запись была создана, отправляем пользователя обратно на страницу книг с сообщением
           # print("Book added to your collection.")
            print("Request!")
            books_request.save()
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