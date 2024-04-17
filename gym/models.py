from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from .models import *
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from django.contrib.auth.models import AbstractUser


class Bill(models.Model):
   
    Due_date  = models.DateField()
    Customer_id  = models.CharField(max_length = 50)
    Mobileno = models.CharField(max_length = 10)
    From_date  = models.DateField()
    To_date  = models.DateField()
    select='--select--'
    OneMonth = 'One Month'
    ThreeMonth = 'Three Month'
    SixMonth = 'Six Month'
    TwelveMonth = 'Twelve Month'
   
    status_CHOICES = [
        (select, '--select--'),
        (OneMonth, 'One Month'),
        (ThreeMonth, 'Three Month'),
         (SixMonth, 'Six Month'),
          (TwelveMonth, 'Twelve Month'),
          
    ]
   
    Package_Type = models.CharField(
        max_length=50,
        choices=status_CHOICES,
        default=select)
    Amount = models.CharField(max_length = 50)
    Payed = models.CharField(max_length = 50)
   
    Morning = 'Morning'
    Evening = 'Evening'
    
    status_CHOICES = [
        (select, '--select--'),
        (Morning, 'Morning'),
        (Evening, 'Evening'),
       
    ]
   
    Batch = models.CharField(
        max_length=50,
        choices=status_CHOICES,
        default=select)
    Paid = 'Paid'
    Pending = 'Pending'
   
    status_CHOICES = [
        (Pending, 'Pending'),
        (Paid, 'Paid'),
        
    ]
   
    status = models.CharField(
        max_length=50,
        choices=status_CHOICES,
        default=Pending)
    def __str__(self):
        return self.Customer_id

class Member(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 30)
    Password=models.CharField(max_length = 20)
    Mobile=models.CharField(max_length = 10)
    Weight=models.CharField(max_length = 20)
    Height=models.CharField(max_length = 20)
    Age=models.CharField(max_length = 20)
    Address=models.CharField(max_length = 50)

    def __str__(self):
        return self.Email
    
# class LeaveRequest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     reason = models.TextField()
#     status = models.CharField(max_length=20, default='Pending')

#     def __str__(self):
#         return f"{self.user.username} - {self.start_date} to {self.end_date}"
    
class LeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.start_date} to {self.end_date}"
    
class Trainer(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 30)
    Password=models.CharField(max_length = 20)
    Mobile=models.CharField(max_length = 10)
    Address=models.CharField(max_length = 50)

    def __str__(self):
        return self.Email


    
class Consultant(models.Model):    
    Name = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 30)
    Password=models.CharField(max_length = 20)
    Mobile=models.CharField(max_length = 10)
    Address=models.CharField(max_length = 50)

    def __str__(self):
        return self.Email

class Diet(models.Model):
    Diet = models.CharField(max_length = 50)
    Solution1 = models.CharField(max_length = 100)
    Solution2 = models.CharField(max_length = 100)
    Process = models.CharField(max_length = 500)
    Description = models.CharField(max_length = 100)
    Other_Notes = models.CharField(max_length = 100)
  
    def __str__(self):
        return self.Diet

class Schedule(models.Model):
    Dayno = models.CharField(max_length = 50)
    Schedule_for = models.CharField(max_length = 100)
    Trainee_level = models.CharField(max_length = 100)
    Process = models.CharField(max_length = 500)
    Description = models.CharField(max_length = 100)
    Other_Notes = models.CharField(max_length = 100)
    def __str__(self):
        return self.Schedule_for

class Store(models.Model):
    Product_name = models.CharField(max_length = 50)
    Product_pic = models.ImageField()
    Price = models.CharField(max_length = 20)
    Product_description = models.CharField(max_length = 500)
  
    def __str__(self):
        return self.Product_name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields if needed
    # For example: profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category1(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name
    
class Subcategory1(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category1, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class Product1(models.Model):
    
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category1, on_delete=models.CASCADE)  # Use ForeignKey to relate to Category
    subcategory = models.ForeignKey(Subcategory1, on_delete=models.CASCADE)  # Use ForeignKey to relate to Subcategory
    stock = models.PositiveIntegerField(default=1, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    product_image = models.ImageField(upload_to='product_images/')
    STATUS_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
    ]


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Stock')

    def save(self, *args, **kwargs):
        # Update the status based on the quantity value
        if self.stock == 0:                                                                                                                                                                 
            self.status = 'Out of Stock'
        else:
            self.status = 'In Stock'

        # Convert self.discount to a float and then calculate the sale price
        self.discount = float(self.discount)  # Convert to float
        self.price = float(self.price)  # Convert to float
        self.sale_price = self.price - (self.price * (self.discount / 100))

        super(Product1, self).save(*args, **kwargs)


    def str(self):
        return self.product_name