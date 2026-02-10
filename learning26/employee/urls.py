from django.urls import path
from . import views

urlpatterns = [
    path('employeeList/', views.employeeList, name='employee_list'),
    path('employeeFilter/', views.employeeFilter, name='employee_filter'),
]
