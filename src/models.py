from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=300, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name}'

    
class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.IntegerField(null=True)
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (('Pending','Pending'), ('Out of Delivery','Out of Delivery'), ('Delivered', 'Delivered'))

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return f'{self.customer.last_name}, {self.customer.first_name} - {self.product.name}'
    