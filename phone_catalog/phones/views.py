from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    data = Phone.objects.all()
    if sort == 'name':
        data = data.order_by('name')
    if sort == 'min_price':
        data = data.order_by('price')
    if sort == 'max_price':
        data = data.order_by('-price')
    context = {'phones': data}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
