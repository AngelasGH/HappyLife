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
    path('contact_us/', views.contact_us, name="contact_us"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('reset/', views.reset, name="reset"),
    path('verification/', views.verification, name="verification"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('successfully_reset/', views.successfully_reset, name="successfully_reset"),
    path('reviews/', views.reviews, name="reviews"),
]
