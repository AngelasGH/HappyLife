# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'store/home.html', context)


def products(request):
    context = {}
    return render(request, 'store/products.html', context)


def view_products(request):
    context = {}
    return render(request, 'store/view_products.html', context)


def view_products_details(request):
    context = {}
    return render(request, 'store/view_products_details.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def faqs(request):
    context = {}
    return render(request, 'store/faqs.html', context)


def about_us(request):
    context = {}
    return render(request, 'store/about_us.html', context)


def contact_us(request):
    context = {}
    return render(request, 'store/contact_us.html', context)
