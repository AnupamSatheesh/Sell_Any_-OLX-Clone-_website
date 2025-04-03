from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Admin(AbstractUser):
    usertype=models.CharField(max_length=50)


class Seller(models.Model):
    fk1=models.ForeignKey(Admin, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, blank=False)
    spic=models.ImageField(upload_to='images/', default='blank-profile-picture-973460_1280.webp')
    age=models.IntegerField()
    gender=models.CharField(max_length=10, blank=False)
    Address=models.CharField(max_length=500, blank=False)
    email=models.EmailField(unique=True)
    number=models.IntegerField(blank=False, unique=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50, blank=False, unique=True)


class Products(models.Model):
    fk2=models.ForeignKey(Seller, on_delete=models.CASCADE)
    image1=models.ImageField(upload_to='images/', blank=False)
    image2=models.ImageField(upload_to='images/', blank=False)
    image3=models.ImageField(upload_to='images/')
    image4=models.ImageField(upload_to='images/')
    image5=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=80, blank=False)
    desc=models.CharField(max_length=500)
    prize=models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.title

class Admin_Deleted_Products(models.Model):
    fk3=models.ForeignKey(Seller, on_delete=models.CASCADE)
    image1=models.ImageField(upload_to='images/', blank=False)
    image2=models.ImageField(upload_to='images/', blank=False)
    image3=models.ImageField(upload_to='images/')
    image4=models.ImageField(upload_to='images/')
    image5=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=80, blank=False)
    desc=models.CharField(max_length=1000)
    prize=models.DecimalField(max_digits=10, decimal_places=1)


class Admin_Deleted_Seller_Account(models.Model):
    name=models.CharField(max_length=50, blank=False)
    age=models.IntegerField()
    gender=models.CharField(max_length=10, blank=False)
    Address=models.CharField(max_length=500, blank=False)
    email=models.EmailField()
    number=models.IntegerField(blank=False)
    username=models.CharField(max_length=50, blank=False)
    password=models.CharField(max_length=50, blank=False)

class Comments(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Buyers(models.Model):
    fk4=models.ForeignKey(Admin, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, blank=False)
    bpic=models.ImageField(upload_to='images/', default='blank-profile-picture-973460_1280.webp')
    age=models.IntegerField()
    gender=models.CharField(max_length=10, blank=False)
    Address=models.CharField(max_length=500, blank=False)
    email=models.EmailField(unique=True)
    number=models.IntegerField(blank=False, unique=True)
    username=models.CharField(max_length=50, blank=False)
    password=models.CharField(max_length=50, blank=False, unique=True)

class Razorpay_Transaction(models.Model):
    fk5=models.ForeignKey(Products, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_signature = models.CharField(max_length=100, null=True, blank=True)

class Traction_History(models.Model):
    image1=models.ImageField(upload_to='images/', blank=False)
    image2=models.ImageField(upload_to='images/', blank=False)
    image3=models.ImageField(upload_to='images/')
    image4=models.ImageField(upload_to='images/')
    image5=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=80, blank=False)
    desc=models.CharField(max_length=1000)
    prize=models.DecimalField(max_digits=10, decimal_places=1)
    seller_name=models.CharField(max_length=50, blank=False)
    seller_age=models.IntegerField()
    seller_gender=models.CharField(max_length=10, blank=False)
    seller_Address=models.CharField(max_length=500, blank=False)
    seller_email=models.EmailField()
    seller_number=models.IntegerField(blank=False)
    buyer_name=models.CharField(max_length=50, blank=False)
    buyer_age=models.IntegerField()
    buyer_gender=models.CharField(max_length=10, blank=False)
    buyer_Address=models.CharField(max_length=500, blank=False)
    buyer_email=models.EmailField()
    buyer_number=models.IntegerField(blank=False)
    date=models.DateTimeField(auto_now_add=True)
    odr_id=models.CharField(max_length=100)
    fkbuyer=models.ForeignKey(Buyers, on_delete=models.CASCADE)
    fkseller=models.ForeignKey(Seller, on_delete=models.CASCADE)