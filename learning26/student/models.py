from django.db import models

# Create your models here.
class studentinfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    class meta:
        db_table="studentinfo"
    
class product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()
    color=models.CharField(null=True)
    status=models.CharField(default=True)

    class meta:
        db_table="product"
    
class games(models.Model):
    game_name=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    platform=models.CharField(max_length=100)
    price=models.FloatField(null=True)

    class meta:
        db_table="games"