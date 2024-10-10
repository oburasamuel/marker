from django.db import models
from users.models import CustomUser
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
