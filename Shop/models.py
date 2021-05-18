from django.db import models
import datetime
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from decimal import Decimal

class Seller(models.Model):

    CATEGORY_CHOICES = (
        ('Wholesaler', 'Wholesaler'),
        ('Distributer', 'Distributer'),
        ('Retailer', 'Retailer'),
        ('Others', 'Others'),
    )
    SUBCATEGORY_CHOICES = (
        ('Electronics', 'Electronics'),
        ('TV & Appliances', 'TV & Appliances'),
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Baby & Kids', 'Baby & Kids'),
        ('Computers', 'Computers'),
        ('Phones & Tablets', 'Phones & Tablets'),
        ('Books', 'Books'),
        ('Accessories', 'Accessories'),
        ('Others', 'Others'),
    )

    seller_id = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', default='profile/def_user.png', blank=True)
    phone = models.CharField(max_length=10)
    dob = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=300)
    gstin = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=100, choices=SUBCATEGORY_CHOICES)
    residential_address = models.TextField(max_length=250)
    permanent_address = models.TextField(max_length=250)
    shop_address = models.TextField(max_length=250)

    def __str__(self):
        return str(self.user)


class Customer(models.Model):
    customer_id = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', default='profile/def_user.png', blank=True)
    phone = models.CharField(max_length=10)
    dob = models.DateField(null=True, blank=True)
    residential_address = models.TextField(max_length=250)
    permanent_address = models.TextField(max_length=250)
    delievery_address = models.TextField(max_length=250)

    def __str__(self):
        return str(self.user)


class Product(models.Model):

    SEASON_CHOICES = (
        ('All', "All Season"),
        ('Spring', "Spring 1 March"),
        ('Summer', "Summer 1 June"),
        ('Autumn', "Autumn 1 September"),
        ('Winter', "Winter 1 December"),
    )

    CATEGORY_CHOICES = (
        ('Electronics', 'Electronics'),
        ('TV & Appliances', 'TV & Appliances'),
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Baby & Kids', 'Baby & Kids'),
        ('Computers', 'Computers'),
        ('Phones & Tablets', 'Phones & Tablets'),
        ('Books', 'Books'),
        ('Accessories', 'Accessories'),
        ('Others', 'Others'),
        ('More', 'More'),
    )

    SUBCATEGORY_CHOICES = (
        ('Electronics', (('Washing Machine', 'Washing Machine'),
                         ('Refrigerators', 'Refrigerators'),
                         ('Mixer Grinder & Juicer', 'Mixer Grinder & Juicer'),
                         ('Others', 'Others'))),
        ('TV & Appliances', (('LCD', 'LCD TV'),
                             ('LED', 'LED TV'),
                             ('LEDSmart', 'LED Smart TV'),
                             ('Others', 'Others'))),
        ('Men', (('Jeans', 'Jeans'),
                 ('Trousers', 'Trousers'),
                 ('Shirts', 'Shirts'),
                 ('T-Shirts', 'T-Shirts'),
                 ('Shoes', 'Shoes'),
                 ('Accessories', 'Accessories'),)),
        ('Women', (('Saree', 'Saree'),
                   ('Jeans', 'Jeans'),
                   ('Tops', 'Tops'),
                   ('Shirts', 'Shirts'),
                   ('T-Shirts', 'T-Shirts'),
                   ('Shoes', 'Shoes'),
                   ('Accessories', 'Accessories'),)),
        ('Kids', (('clothes for upto 2yrs kids', 'clothes for upto 2yrs kids'),
                  ('clothes for upto 5yrs kids', 'clothes for upto 5yrs kids'),
                  ('clothes for upto 10yrs kids', 'clothes for upto 10yrs kids'),
                  ('clothes for upto 15yrs kids', 'clothes for upto 15yrs kids'),
                  ('clothes for above 15yrs kids', 'clothes for above 15yrs kids'),)),
        ('Computers', (('PC', 'PC'),
                       ('Laptops', 'Laptops'),
                       ('Accessories', 'Accessories'),
                       ('Others', 'Others'))),
        ('Phones & Tablets', (('Bar Phones', 'Bar Phones'),
                              ('Smartphones', 'Smartphones'),
                              ('Smart Tablets', 'Smart Tablets'),
                              ('Others', 'Others'))),
        ('Books', (('Literature', 'Literature'),
                   ('Comics', 'Comics'),
                   ('Story', 'Story'),
                   ('Biography', 'Biography'),
                   ('Educational', 'Educational'),
                   ('Others', 'Others'),)),
        ('Accessories', (('PC', 'PC'),
                         ('Laptops', 'Laptops'),
                         ('Phones', 'Phones'),
                         ('Others', 'Others'),)),
        ('Others', 'Others'),
    )

    TYPE_CHOICES = (
        ('None', 'None'),
        ('New', 'New Arrivals'),
        ('Trending', 'Trending'),
        ('Sales', 'Sales'),
        ('Regular', 'Regular Use'),
        ('Party', 'Party Wear'),
        ('Ethnic', 'Ethnic Wear'),
    )
    
    product_id = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', blank=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('1.00'))
    in_stock = models.BooleanField(default=True)
    stock_qty = models.IntegerField(blank=False)
    reorder_qty = models.IntegerField(blank=False)
    is_discount = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=100, choices=SUBCATEGORY_CHOICES)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES)
    type_choice = models.CharField(max_length=20, choices=TYPE_CHOICES)
    exp_date = models.DateField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=Decimal('0.0'), validators=[MaxValueValidator(5.0)])

    def __str__(self):
        return str(self.product_id)


class Order(models.Model):

    STATUS_CHOICES = (
        ('NA', '--Not-Available--'),
        ('Ordered', 'Ordered'),
        ('Packed', 'Packed'),
        ('Shipped', 'Shipped'),
        ('Delievered', 'Delievered'),
        ('Cancelled', 'Cancelled'),
    )
    orderid = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='NA')
    invoice = models.IntegerField(default=0)
    no_of_items = models.IntegerField(default=0)
    order_date = models.DateField(blank=True, null=True)
    shipping_date = models.DateField(blank=True, null=True)
    shipping_address = models.TextField(max_length=250)

    is_complete = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    deliever_date = models.DateField(blank=True, null=True)

    transaction_id = models.CharField(max_length=20, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orderid)


class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order)
