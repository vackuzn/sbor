from cart.cart import Cart
from main.models import SiteSettings


def cart(request):
    cart = Cart(request)
    min_sum = int(SiteSettings.objects.get(id=1).value)
    context = {'cart': cart, 'min_sum': min_sum}
    return context
