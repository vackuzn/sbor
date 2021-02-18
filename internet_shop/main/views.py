from django.shortcuts import render
from django.http import HttpResponse
from main.models import Category, Product


def main_page(request):
    return render(request, 'main/main_page.html')


def categories(request):
    all_categories = Category.objects.all()
    context = {'all_categories': all_categories}
    return render(request, 'main/categories.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    all_products = Product.objects.filter(category=category)
    context = {'category': category, 'all_products': all_products}
    return render(request, 'main/category.html', context)