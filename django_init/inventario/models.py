from django.db import models

# Create your models here.


class Bodega(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    description = models.CharField(max_length=254, null=True)
    stock = models.IntegerField()
    bodega_id = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
