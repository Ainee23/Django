from django.urls import path
from . import views

urlpatterns = [
    path('employeeList/', views.employeeList, name='employee_list'),
    path('employeeFilter/', views.employeeFilter, name='employee_filter'),
    path('createemployee/',views.createEmployee),
    path('createEmployeeWithForm/',views.createEmployeeWithForm),
    path('createCourse/',views.createCourse),
    path('createStudent/',views.createstudent),
    path('createCar/', views.createCar),
    
]
