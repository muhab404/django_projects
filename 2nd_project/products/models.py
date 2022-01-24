from django.db import models

# Create your models here.

class Product(models.Model):

    x = [
        ('phone','phone'),
        ('computer','computer'),
    ]
    name = models.CharField(max_length=50)
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photes/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True,blank=True,choices=x)

    def __str__(self):
        return self.name

    class  Meta:
        ordering=['name']   


