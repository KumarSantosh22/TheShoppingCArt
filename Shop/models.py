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
        ('0', "All Season"),
        ('1', "Spring 1 March"),
        ('2', "Summer 1 June"),
        ('3', "Autumn 1 September"),
        ('4', "Winter 1 December"),
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
        ('Kids', (('0', 'clothes for upto 2yrs kids'),
                  ('1', 'clothes for upto 5yrs kids'),
                  ('2', 'clothes for upto 10yrs kids'),
                  ('3', 'clothes for upto 15yrs kids'),
                  ('4', 'clothes for above 15yrs kids'),)),
        ('Computers', (('PC', 'PC'),
                       ('Laptops', 'Laptops'),
                       ('Accessories', 'Accessories'),
                       ('Others', 'Others'))),
        ('Phones & Tablets', (('0', 'Bar Phones'),
                              ('1', 'Smartphones'),
                              ('2', 'Smart Tablets'),
                              ('3', 'Others'))),
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
        ('0', 'None'),
        ('1', 'New Arrivals'),
        ('2', 'Trending'),
        ('3', 'Sales'),
        ('4', 'Regular Use'),
        ('5', 'Party Wear'),
        ('6', 'Ethnic Wear'),
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
    rating = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return str(self.product_id)


class Order(models.Model):

    STATUS_CHOICES = (
        ('NA', '--Not-Available--'),
        ('1', 'Ordered'),
        ('2', 'Packed'),
        ('3', 'Shipped'),
        ('4', 'Delievered'),
        ('9', 'Cancelled'),
    )
    orderid = models.IntegerField(
        primary_key=True, blank=False, auto_created=True)
    status1 = models.CharField(max_length=20, choices=STATUS_CHOICES)
    status2 = models.CharField(max_length=20, choices=STATUS_CHOICES)
    status3 = models.CharField(max_length=20, choices=STATUS_CHOICES)
    status4 = models.CharField(max_length=20, choices=STATUS_CHOICES)
    invoice = models.IntegerField()
    no_of_items = models.IntegerField()
    order_date = models.DateField(blank=True, null=True)
    shipping_date = models.DateField(blank=True, null=True)
    shipping_address = models.TextField(max_length=250)

    is_shipped = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    deliever_date  = models.DateField(blank=True, null=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orderid)
