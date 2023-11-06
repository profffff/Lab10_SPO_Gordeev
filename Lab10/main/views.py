from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    data = {
        'title': 'Main',
        'values': ['one', 'two', 'three'],
        'obj': {
            'car': 'Mers',
            'age': 12
        }
    }
    return render(request, 'main/index.html', data)


@login_required
def about(request):
    return render(request, 'main/about.html')



