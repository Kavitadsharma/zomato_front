from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Dish, Order, OrderDish
from .forms import OrderStatusForm

def menu_management(request):
    dishes = Dish.objects.all()
    return render(request, 'zomato_app/menu_management.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST['dish_name']
        price = request.POST['price']
        availability = request.POST.get('availability', False) == 'on'  
        new_dish = Dish.objects.create(dish_name=dish_name, price=price, availability=availability)
        return redirect('menu_management')


def remove_dish(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    dish.delete()
    return redirect('menu_management')

def toggle_availability(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    dish.availability = not dish.availability
    dish.save()
    return redirect('menu_management')

def create_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        dish_ids = request.POST.getlist('dishes')
        
        order = Order.objects.create(customer_name=customer_name)
        for dish_id in dish_ids:
            dish = Dish.objects.get(pk=dish_id)
            OrderDish.objects.create(order=order, dish=dish)
        
        return redirect('order_status')

def update_order_status(request, order_id):
    order = Order.objects.get(pk=order_id)
    if request.method == 'POST':
        order_status_form = OrderStatusForm(request.POST, instance=order)
        if order_status_form.is_valid():
            order_status_form.save()
            return redirect('order_status')
    else:
        order_status_form = OrderStatusForm(instance=order)
    
    return render(request, 'zomato_app/update_order_status.html', {'order': order, 'form': order_status_form})

def order_status(request):
    orders = Order.objects.all()
    return render(request, 'zomato_app/order_status.html', {'orders': orders})
