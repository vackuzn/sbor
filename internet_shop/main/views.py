from django.shortcuts import render
from django.http import HttpResponse
from main.models import Category


def main_page(request):
    return render(request, 'main/main_page.html')


def categories(request):
    all_categories = Category.objects.all()
    context = {'all_categories': all_categories}
    return render(request, 'main/categories.html', context)


def category(request, id):
    category = Category.objects.get(id=id)
    context = {'category': category}
    return render(request, 'main/category.html', context)