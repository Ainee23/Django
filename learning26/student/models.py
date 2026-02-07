from django.db import models

# Create your models here.
class studentinfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    class meta:
        db_table="studentinfo"
    def __str__(self):
        return self.name
    
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
class studentprofile(models.Model):
    studentid=models.OneToOneField(studentinfo,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    
    class meta:
        db_table="studentprofile"

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName

class employee(models.Model):
    employeeName = models.CharField(max_length=100)
    employeeEmail = models.EmailField()
    employeePhone = models.CharField(max_length=100)
    employeeSalary = models.IntegerField()
    employeeStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.employeeName

class employeeprofile(models.Model):
    employeeId = models.OneToOneField(employee,on_delete=models.CASCADE)
    employeeAddress = models.CharField(max_length=100)
    employeePosition = models.CharField(max_length=100)

    class Meta:
        db_table = "employeeprofile"

    def __str__(self):
        return self.employeeId.employeeName

class user(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username
    
class order(models.Model):
    orderNumber = models.CharField(max_length=100)
    orderDate = models.DateField()
    orderStatus = models.BooleanField(default=True)
    userId = models.ForeignKey(user,on_delete=models.CASCADE)

    class Meta:
        db_table = "order"

    def __str__(self):
        return self.orderNumber
    
class country(models.Model):
    countryName = models.CharField(max_length=100)
    countryCode = models.CharField(max_length=10)

    class Meta:
        db_table = "country"

    def __str__(self):
        return self.countryName
    
class city(models.Model):
    cityName = models.CharField(max_length=100)
    cityCode = models.CharField(max_length=10)
    countryId = models.ForeignKey(country,on_delete=models.CASCADE)

    class Meta:
        db_table = "city"

    def __str__(self):
        return self.cityName