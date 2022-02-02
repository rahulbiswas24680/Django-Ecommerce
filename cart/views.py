from django.shortcuts import render
from shop.models import Product
from .models import Order
from django.shortcuts import redirect
from django.contrib import messages





def cart_detail(request):
    if request.session.get('cart') == {}:
        cart_empty = True
    else:
        cart_products = Product.objects.filter(id__in=list(request.session['cart'].keys())).reverse()
        
        context = {
            'cart_products': cart_products,
            'range': range(1, 15)
            }
        return render(request, 'cart/cart_detail.html', context=context)
    
    return render(request, 'cart/cart_detail.html', context={'cart_empty': cart_empty})



def clear_cart(request):
    del request.session['cart']
    request.session.get('cart') == {}
    cart_empty = True
    print(request.session.get('cart'))
    return render(request, 'cart/cart_detail.html', context={'cart_empty': cart_empty})




def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        address = request.POST.get('address', '') + '/' + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pin = request.POST.get('pin', '')
        phone = request.POST.get('phone', '')
        cart = request.session['cart']
        customer_id = request.session['customer'].get('id')
        products = Product.objects.filter(id__in=list(cart.keys()))
        for product in products:
            order = Order(
                customer=name,
                customer_id=customer_id,
                address=address,
                city=city,
                state=state,
                pin=pin,
                phone=phone,
                product=product,
                quantity=cart[str(product.id)],
                price=product.price
                )
            order.place_order()
        del request.session['cart']
        return redirect('home')
        messages.add_message(request, messages.SUCCESS, 'Successfully! Your order has been placed.')
    return render(request, 'cart/checkout.html')



def order_list(request):
    customer_id = request.session['customer'].get('id')
    if Order.objects.all() == None:
        order_empty = True
    else:
        orders = Order.objects.filter(customer_id=customer_id)
    return render(request, 'cart/order.html', {'orders': orders})
