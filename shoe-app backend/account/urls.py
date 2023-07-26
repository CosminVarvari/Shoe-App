from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('manager_register/',views.manager_register.as_view(), name='manager_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('admin_register/', views.admin_register.as_view(), name='admin_register'),
     path('logout/',views.logout_view, name='logout'),
     path('add/', views.add_user),
     path('', views.view_users),
     path('detail/<int:pk>/', views.detail_user),
     path('update/',views.update_user),
     path('delete/<int:pk>/', views.delete_user),
     path('login/', views.login_user),
]