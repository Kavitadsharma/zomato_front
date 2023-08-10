from django.db import models

# Create your models here.
from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.dish_name

class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    dishes = models.ManyToManyField(Dish, through='OrderDish')
    status = models.CharField(
        max_length=20,
        choices=[
            ('received', 'Received'),
            ('preparing', 'Preparing'),
            ('ready', 'Ready for Pickup'),
            ('delivered', 'Delivered')
        ],
        default='received'
    )

    def __str__(self):
        return f"Order for {self.customer_name} ({self.get_status_display()})"

class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order} - {self.dish}"
