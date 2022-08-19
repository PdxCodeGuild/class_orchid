from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # entree = models.Choices()
    # add_ons = models.Choices()
    
    
# order = Order.objects.get(id=1)
# new_order = Order(first_name='first_name', last_name='last_name')
# new_order.save()