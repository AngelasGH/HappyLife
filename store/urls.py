from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('view_products/', views.view_products, name="view_products"),
    path('view_products_details/', views.view_products_details, name="view_products_details"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('faqs/', views.faqs, name="faqs"),
    path('about_us/', views.about_us, name="about_us"),
    path('contact_us/', views.contact_us, name="contact_us")
]
