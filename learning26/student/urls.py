from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('marksheet/', views.marksheet),
    path('info/',views.information)
]
