from django.db import models



class Product(models.Model):
    model = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.CharField(max_length=200)
    urls = models.CharField(max_length=400)
    description = models.TextField()
    images1 = models.ImageField(upload_to='static/images.costumers/', default='default_image.jpg')
    images2 = models.ImageField(upload_to='static/images.costumers/', default='default_image.jpg')
    images3 = models.ImageField(upload_to='static/images.costumers/', default='default_image.jpg')
    office = models.CharField(max_length=200, default=0)
    operating_system = models.CharField(max_length=200, default=0)
    mobileness= models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return self.model
  