from django.urls import path
from . import views

urlpatterns = [
    path('employeeList/', views.employeeList, name='employee_list'),
    path('employeeFilter/', views.employeeFilter, name='employee_filter'),
  
    path('createemployee/', views.createEmployee, name='create_employee'),
    path('createEmployeeWithForm/', views.createEmployeeWithForm, name='create_employee_with_form'),

    path('createCourse/', views.createCourse, name='create_course'),
    path('createStudent/', views.createstudent, name='create_student'),
    path('createCar/', views.createCar, name='create_car'),

    path('deleteEmployee/<int:id>/', views.deleteEmployee, name='delete_employee'),
    path('filterEmployee/', views.filterEmployee, name='filter_employee'),
    path("sortemployees/<int:id>/", views.sortemployees, name="sortemployees")

]
