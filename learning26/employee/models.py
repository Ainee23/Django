from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee_master"

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    class Meta:
        db_table = "course"
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE) #course_id
    class Meta:
        db_table = "student"
    def __str__(self):
        return self.name
    
class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    fuel_type = models.CharField(max_length=50)

    class Meta:
        db_table = "CAR"

    def __str__(self):
        return f"{self.brand} {self.model}"