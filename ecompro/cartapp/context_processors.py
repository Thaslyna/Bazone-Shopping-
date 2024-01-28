from .models import Cart, CartItem
from .views import cart_id1
from django.core.exceptions import ObjectDoesNotExist


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=cart_id1(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items :
                item_count += cart_item.quantity
        except DoesNotExist:
            item_count = 0
    return {'item_count': item_count}
