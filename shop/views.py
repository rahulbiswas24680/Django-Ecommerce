from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Category, Contact
from django.utils import timezone
import uuid


uuid_generator = uuid.uuid1()


class HomeListView(ListView):
    template_name = 'shop/home.html'

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart')
        customer = request.session.get('customer')
        if not cart:
            request.session['cart'] = {}
        if not customer:
            request.session['customer'] = {'id': str(uuid_generator)}
        # del request.session['cart']                   ## to delete all cart-items
        # del request.session['customer']
        return super().get(request, *args, **kwargs)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # session cart logic here
        cart = request.session.get('cart')
        if cart:
            keys = list(cart.keys())
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        # print(cart)

        return redirect('home')

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context


class ProductListView(ListView): 
    template_name = 'shop/product_list.html'
    context_object_name = 'category_products'

    def post(self, request, *args, **kwargs):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # session cart logic here
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        return redirect('category-products', category_slug=self.kwargs.get('category_slug'))

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('category_slug')) 
        context['category'] = category
        context['products'] = Product.objects.filter(category=category)
        return context


        

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    
    def post(self, request, *args, **kwargs):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # session cart logic here
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        return redirect('product-detail', id=self.kwargs.get('id'), slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, id=self.kwargs.get('id'), slug=self.kwargs.get('slug'), available=True)
        return context




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('messages')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return redirect('home')
        messages.add_message(request, messages.SUCCESS, 'Your message has been send.')
    return render(request, 'shop/contact.html')


def about(request):
    return render(request, 'shop/about.html')



