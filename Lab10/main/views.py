from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from database.models import Articles
import math
from django import template

register = template.Library()

@register.filter(name='range')
def filter_range(x):
    return range(x)


@login_required
def index(request):
    databases = Articles.objects.all()
    return render(request, 'main/index.html', {'databases': databases})


@login_required
def about(request):
    return render(request, 'main/about.html')



