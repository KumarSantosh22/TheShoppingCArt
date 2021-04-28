# Generated by Django 3.1.7 on 2021-04-28 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=500)),
                ('password', models.CharField(max_length=20)),
                ('delievery_address', models.TextField(max_length=250)),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('description', models.TextField(max_length=300)),
                ('gstin', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Wholesaler', 'Wholesaler'), ('Distributer', 'Distributer'), ('Retailer', 'Retailer'), ('Others', 'Others')], max_length=100)),
                ('subcategory', models.CharField(choices=[('Electronics', 'Electronics'), ('TV & Appliances', 'TV & Appliances'), ('Men', 'Men'), ('Women', 'Women'), ('Baby & Kids', 'Baby & Kids'), ('Computers', 'Computers'), ('Phones & Tablets', 'Phones & Tablets'), ('Books', 'Books'), ('Accessories', 'Accessories'), ('Others', 'Others')], max_length=100)),
                ('address', models.TextField(max_length=250)),
                ('permanent_address', models.TextField(max_length=250)),
                ('shop_address', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('stock_qty', models.IntegerField()),
                ('reorder_qty', models.IntegerField()),
                ('is_discount', models.BooleanField(default=False)),
                ('discount', models.IntegerField()),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('TV & Appliances', 'TV & Appliances'), ('Men', 'Men'), ('Women', 'Women'), ('Baby & Kids', 'Baby & Kids'), ('Computers', 'Computers'), ('Phones & Tablets', 'Phones & Tablets'), ('Books', 'Books'), ('Accessories', 'Accessories'), ('Others', 'Others'), ('More', 'More')], max_length=100)),
                ('subcategory', models.CharField(choices=[('Electronics', (('Washing Machine', 'Washing Machine'), ('Refrigerators', 'Refrigerators'), ('Mixer Grinder & Juicer', 'Mixer Grinder & Juicer'), ('Others', 'Others'))), ('TV & Appliances', (('LCD', 'LCD TV'), ('LED', 'LED TV'), ('LEDSmart', 'LED Smart TV'), ('Others', 'Others'))), ('Men', (('Jeans', 'Jeans'), ('Trousers', 'Trousers'), ('Shirts', 'Shirts'), ('T-Shirts', 'T-Shirts'), ('Shoes', 'Shoes'), ('Accessories', 'Accessories'))), ('Women', (('Saree', 'Saree'), ('Jeans', 'Jeans'), ('Tops', 'Tops'), ('Shirts', 'Shirts'), ('T-Shirts', 'T-Shirts'), ('Shoes', 'Shoes'), ('Accessories', 'Accessories'))), ('Kids', (('0', 'clothes for upto 2yrs kids'), ('1', 'clothes for upto 5yrs kids'), ('2', 'clothes for upto 10yrs kids'), ('3', 'clothes for upto 15yrs kids'), ('4', 'clothes for above 15yrs kids'))), ('Computers', (('PC', 'PC'), ('Laptops', 'Laptops'), ('Accessories', 'Accessories'), ('Others', 'Others'))), ('Phones & Tablets', (('0', 'Bar Phones'), ('1', 'Smartphones'), ('2', 'Smart Tablets'), ('3', 'Others'))), ('Books', (('Literature', 'Literature'), ('Comics', 'Comics'), ('Story', 'Story'), ('Biography', 'Biography'), ('Educational', 'Educational'), ('Others', 'Others'))), ('Accessories', (('PC', 'PC'), ('Laptops', 'Laptops'), ('Phones', 'Phones'), ('Others', 'Others'))), ('Others', 'Others')], max_length=100)),
                ('season', models.CharField(choices=[('0', 'All Season'), ('1', 'Spring 1 March'), ('2', 'Summer 1 June'), ('3', 'Autumn 1 September'), ('4', 'Winter 1 December')], max_length=20)),
                ('type', models.CharField(choices=[('0', 'None'), ('1', 'New Arrivals'), ('2', 'Trending'), ('3', 'Sales'), ('4', 'Regular Use'), ('5', 'Party Wear'), ('6', 'Ethnic Wear')], max_length=20)),
                ('exp_date', models.DateField(default=None, null=True)),
                ('image', models.ImageField(blank=True, upload_to='product/')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('status1', models.CharField(choices=[('NA', '--Not-Available--'), ('1', 'Ordered'), ('2', 'Packed'), ('3', 'Shipped'), ('4', 'Delievered'), ('9', 'Cancelled')], max_length=20)),
                ('status2', models.CharField(choices=[('NA', '--Not-Available--'), ('1', 'Ordered'), ('2', 'Packed'), ('3', 'Shipped'), ('4', 'Delievered'), ('9', 'Cancelled')], max_length=20)),
                ('status3', models.CharField(choices=[('NA', '--Not-Available--'), ('1', 'Ordered'), ('2', 'Packed'), ('3', 'Shipped'), ('4', 'Delievered'), ('9', 'Cancelled')], max_length=20)),
                ('status4', models.CharField(choices=[('NA', '--Not-Available--'), ('1', 'Ordered'), ('2', 'Packed'), ('3', 'Shipped'), ('4', 'Delievered'), ('9', 'Cancelled')], max_length=20)),
                ('invoice', models.IntegerField()),
                ('no_of_items', models.IntegerField()),
                ('order_date', models.DateField()),
                ('shipping_date', models.DateField()),
                ('shipping_address', models.TextField(max_length=250)),
                ('is_shipped', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('deliever_date', models.DateField(blank=True, null=True)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.customer')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
                ('sellerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.seller')),
            ],
        ),
    ]
