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
    # view_products
    path('butterfly/', views.butterfly, name="butterfly"),
    path('butterfly_details/', views.butterfly_details, name="butterfly_details"),
    path('chamomile/', views.chamomile, name="chamomile"),
    path('chamomile_details/', views.chamomile_details, name="chamomile_details"),
    path('green_tea/', views.green_tea, name="green_tea"),
    path('green_tea_details/', views.green_tea_details, name="green_tea_details"),
    path('lapsang/', views.lapsang, name="lapsang"),
    path('lapsang_details/', views.lapsang_details, name="lapsang_details"),
    # user_view
    path('user_home/', views.user_home, name="user_home"),
    path('user_products/', views.user_products, name="user_products"),
    path('user_view_products/', views.user_view_products, name="user_view_products"),
    path('user_view_products_details/', views.user_view_products_details, name="user_view_products_details"),
    path('user_cart/', views.user_cart, name="user_cart"),
    path('user_checkout/', views.user_checkout, name="user_checkout"),
    path('user_faqs/', views.user_faqs, name="user_faqs"),
    path('user_about_us/', views.user_about_us, name="user_about_us"),
    path('user_contact_us/', views.user_contact_us, name="user_contact_us"),
    path('user_register/', views.user_register, name="user_register"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_reset/', views.user_reset, name="user_reset"),
    path('user_verification/', views.user_verification, name="user_user_verification"),
    path('user_reset_password/', views.user_reset_password, name="user_reset_password"),
    path('user_successfully_reset/', views.user_successfully_reset, name="user_successfully_reset"),
    path('user_reviews/', views.user_reviews, name="user_reviews"),
    # view_products
    path('user_butterfly/', views.user_butterfly, name="user_butterfly"),
    path('user_butterfly_details/', views.user_butterfly_details, name="user_butterfly_details"),
    path('user_chamomile/', views.user_chamomile, name="user_chamomile"),
    path('user_chamomile_details/', views.user_chamomile_details, name="user_chamomile_details"),
    path('user_green_tea/', views.user_green_tea, name="user_green_tea"),
    path('user_green_tea_details/', views.user_green_tea_details, name="user_green_tea_details"),
    path('user_lapsang/', views.user_lapsang, name="user_lapsang"),
    path('user_lapsang_details/', views.user_lapsang_details, name="user_lapsang_details"),
    # Payments
    path('cash_on/', views.cash_on, name="cash_on"),
    path('credit_debit/', views.credit_debit, name="credit_debit"),
    path('credit_debit_ready_to_place/', views.credit_debit_ready_to_place, name="credit_debit_ready_to_place"),
    path('e_wallet/', views.e_wallet, name="e_wallet"),
    # Purchases
    path('to_receive/', views.to_receive, name="to_receive"),
    path('purchase_details/', views.purchase_details, name="purchase_details"),
    path('details/', views.details, name="details"),
    path('order_received/', views.order_received, name="order_received"),
]
