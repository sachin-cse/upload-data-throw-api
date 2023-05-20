from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student_details/<int:pk>/', views.student_details, name='student_details')
]