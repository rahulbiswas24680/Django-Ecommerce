from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ " + str(number)


@register.filter(name='multiply')
def multiply(qty, number):
    return qty * number

@register.filter(name='customer_total_cost')
def customer_total_cost(orders):
    sum = 0
    for order in orders:
        sum += (order.price * order.quantity)
    return sum