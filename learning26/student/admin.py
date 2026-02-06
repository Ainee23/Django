from django.contrib import admin
from .models import studentinfo, product, games, studentprofile, Category, Service, employee, employeeprofile, user, order, country, city
# Register your models here.
admin.site.register(studentinfo)
admin.site.register(product)
admin.site.register(games)
admin.site.register(studentprofile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(employee)
admin.site.register(employeeprofile)
admin.site.register(user)
admin.site.register(order)
admin.site.register(country)
admin.site.register(city)

