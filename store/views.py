from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'store/home.html', context)


def products(request):
    context = {}
    return render(request, 'store/products.html', context)


def view_products(request):
    context = {}
    return render(request, 'store/green_tea.html', context)


def view_products_details(request):
    context = {}
    return render(request, 'store/green_tea_details.html', context)


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


def register(request):
    context = {}
    return render(request, 'Register_login/register.html', context)


def login(request):
    context = {}
    return render(request, 'Register_login/login.html', context)


def reset(request):
    context = {}
    return render(request, 'Register_login/reset.html', context)


def verification(request):
    context = {}
    return render(request, 'Register_login/verification.html', context)


def reset_password(request):
    context = {}
    return render(request, 'Register_login/reset_password.html', context)


def successfully_reset(request):
    context = {}
    return render(request, 'Register_login/successfully_reset.html', context)


def reviews(request):
    context = {}
    return render(request, 'store/reviews.html', context)


def butterfly(request):
    context = {}
    return render(request, 'view_products/butterfly.html', context)


def butterfly_details(request):
    context = {}
    return render(request, 'view_products/butterfly_details.html', context)


def chamomile(request):
    context = {}
    return render(request, 'view_products/chamomile.html', context)


def chamomile_details(request):
    context = {}
    return render(request, 'view_products/chamomile_details.html', context)


def green_tea(request):
    context = {}
    return render(request, 'view_products/green_tea.html', context)


def green_tea_details(request):
    context = {}
    return render(request, 'view_products/green_tea_details.html', context)


def lapsang(request):
    context = {}
    return render(request, 'view_products/lapsang.html', context)


def lapsang_details(request):
    context = {}
    return render(request, 'view_products/lapsang_details.html', context)


# user_view
def user_home(request):
    context = {}
    return render(request, 'user/home.html', context)


def user_products(request):
    context = {}
    return render(request, 'user/products.html', context)


def user_view_products(request):
    context = {}
    return render(request, 'user/green_tea.html', context)


def user_view_products_details(request):
    context = {}
    return render(request, 'user/green_tea_details.html', context)


def user_cart(request):
    context = {}
    return render(request, 'user/cart.html', context)


def user_checkout(request):
    context = {}
    return render(request, 'user/checkout.html', context)


def user_faqs(request):
    context = {}
    return render(request, 'user/faqs.html', context)


def user_about_us(request):
    context = {}
    return render(request, 'user/about_us.html', context)


def user_contact_us(request):
    context = {}
    return render(request, 'user/contact_us.html', context)


def user_register(request):
    context = {}
    return render(request, 'Register_login/register.html', context)


def user_login(request):
    context = {}
    return render(request, 'Register_login/login.html', context)


def user_reset(request):
    context = {}
    return render(request, 'Register_login/reset.html', context)


def user_verification(request):
    context = {}
    return render(request, 'Register_login/verification.html', context)


def user_reset_password(request):
    context = {}
    return render(request, 'Register_login/reset_password.html', context)


def user_successfully_reset(request):
    context = {}
    return render(request, 'Register_login/successfully_reset.html', context)


def user_reviews(request):
    context = {}
    return render(request, 'user/reviews.html', context)


def user_butterfly(request):
    context = {}
    return render(request, 'user_view_products/butterfly.html', context)


def user_butterfly_details(request):
    context = {}
    return render(request, 'user_view_products/butterfly_details.html', context)


def user_chamomile(request):
    context = {}
    return render(request, 'user_view_products/chamomile.html', context)


def user_chamomile_details(request):
    context = {}
    return render(request, 'user_view_products/chamomile_details.html', context)


def user_green_tea(request):
    context = {}
    return render(request, 'user_view_products/green_tea.html', context)


def user_green_tea_details(request):
    context = {}
    return render(request, 'user_view_products/green_tea_details.html', context)


def user_lapsang(request):
    context = {}
    return render(request, 'user_view_products/lapsang.html', context)


def user_lapsang_details(request):
    context = {}
    return render(request, 'user_view_products/lapsang_details.html', context)


def cash_on(request):
    context = {}
    return render(request, 'payments/cash_on.html', context)


def credit_debit(request):
    context = {}
    return render(request, 'payments/credit_debit.html', context)


def credit_debit_ready_to_place(request):
    context = {}
    return render(request, 'payments/credit_debit_ready_to_place.html', context)


def e_wallet(request):
    context = {}
    return render(request, 'payments/e_wallet.html', context)


def to_receive(request):
    context = {}
    return render(request, 'purchase/to_receive.html', context)


def purchase_details(request):
    context = {}
    return render(request, 'purchase/purchase_details.html', context)


def details(request):
    context = {}
    return render(request, 'purchase/details.html', context)


def order_received(request):
    context = {}
    return render(request, 'purchase/order_received.html', context)
