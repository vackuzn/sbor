from django.shortcuts import render
from django.http import HttpResponse
from main.models import Category, Product
from django.db.models import Count, F
from django.core.paginator import Paginator


def main_page(request):
    return render(request, 'main/main_page.html')


def categories(request):
    all_categories = Category.objects.annotate(x=Count('product')).filter(x__gt=0)
    context = {'all_categories': all_categories}
    return render(request, 'main/categories.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    all_products = Product.objects.filter(category=category, is_published=True)

    # счетчик посещений этой категории
    if request.GET.get('page') == None:
        category.views = F('views') + 1
    category.save()

    # пагинация
    paginator = Paginator(all_products, 4)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {'category': category, 'page_obj': page_obj}
    return render(request, 'main/category.html', context)


def product_card(request, pk):
    product = Product.objects.get(pk=pk)
    additional_pictures = product.imagegallery_set.all()
    context = {'product': product, 'additional_pictures': additional_pictures}

    print(additional_pictures)
    for i in additional_pictures:
        print(i.additional_picture)

    return render(request, 'main/product_card.html', context)




