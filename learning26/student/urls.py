from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('marksheet/', views.marksheet),
    path('info/',views.information),
    path("serviceList/",views.serviceList,name="serviceList"),
    path("createService/",views.createService,name="createService"),
    path("deleteService/<int:id>/", views.deleteService, name="deleteService"),

]
