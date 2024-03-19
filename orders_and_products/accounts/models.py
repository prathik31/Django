from django.db import models

# Create your models here.

class tag(models.Model):
    name=models.CharField( max_length=50)

    def __str__(self):
        return self.name
    

class products(models.Model):
    CATEGORY=(
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )
    prod_name=models.CharField(max_length=50)
    prod_price=models.FloatField()
    prod_category=models.CharField(max_length=50, choices=CATEGORY, blank=True)
    prod_desc=models.CharField(max_length=100)
    date_created=models.DateField(auto_now_add=True)
    TAGS=models.ManyToManyField(tag, blank=True)

    def __str__(self):
        return self.prod_name
    

class customer(models.Model):
    name=models.CharField( max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=254)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered')
    )

    CUSTOMER=models.ForeignKey(customer, null=True, on_delete=models.SET_NULL)
    PRODUCT=models.ForeignKey(products, null=True, on_delete=models.SET_NULL)
    status=models.CharField(max_length=50, choices=STATUS)
    date_create=models.DateTimeField( auto_now_add=True)

    def __str__(self) -> str:
        return self.PRODUCT.prod_name