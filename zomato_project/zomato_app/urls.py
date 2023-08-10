from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_management, name='menu_management'),
    path('menu/', views.menu_management, name='menu_management'),
    path('menu/add/', views.add_dish, name='add_dish'),
    path('menu/remove/<int:dish_id>/', views.remove_dish, name='remove_dish'),
    path('menu/toggle/<int:dish_id>/', views.toggle_availability, name='toggle_availability'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('order/status/', views.order_status, name='order_status'),
]
