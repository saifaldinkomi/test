from django.db import models

# Create your models here.
class CUSTOMER(models.Model):
    name=models.CharField( max_length=90,null=True )
    email=models.CharField(max_length=90,null=True )
    age=models.FloatField(null=True )
    data_created=models.DateField(auto_now_add=True ,null=True )
    def __str__(self):
        return self.name
    
class BOOK(models.Model):
    CATEGORIES=(
        ("Thriller","Thriller"),
        ("Historical Fiction","Historical Fiction"),
        ("hororr","horoor"),
    )
    name=models.CharField( max_length=90,null=True)
    author=models.CharField(max_length=90,null=True)
    price=models.FloatField(null=True)
    catecogy=models.CharField(max_length=90,null=True,choices= CATEGORIES)
    data_created=models.DateField(auto_now_add=True ) 
    def __str__(self):
        return self.name
    
class TAG(models.Model):
    name=models.CharField(max_length=90,null=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS=(
        ("pindeing","pinding"),
        ("delivered","delivered"),
        ("out of order","out of order")
    )
    book=models.ForeignKey(BOOK,on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey(CUSTOMER, on_delete=models.SET_NULL,null=True)
    status=models.CharField( max_length=90,null=True,choices=STATUS)
    tag=models.ManyToManyField(TAG)
    data_created=models.DateField( auto_now_add=True,null=True)