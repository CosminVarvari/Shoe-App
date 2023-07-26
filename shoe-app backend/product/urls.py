from django.urls import path

from . import views
from .views import *
urlpatterns = [
    path('add/', views.add_products),
    path('', views.view_products),
    path('detail/<int:pk>/', views.detail_product),
    path('update/',views.update_product),
    path('delete/<int:pk>/', views.delete_product),
    path('search/', views.searchBar, name='search'),
    path('employee/savecsv', views.export_csv_employee, name='employeecsv'),
    path('employee/saveJson', views.export_json_employee, name='employeejson'),
    path('employee/savetxt', views.export_txt_employee, name='employeetxt'),
    path('employee/savexml', views.export_xml_employee, name='employeexml'),
    path('manager/savecsv', views.export_csv_manager, name='managercsv'),
    path('manager/saveJson', views.export_json_manager, name='managerjson'),
    path('manager/savetxt', views.export_txt_manager, name='managertxt'),
    path('manager/savexml', views.export_xml_manager, name='managerxml'),
    path('manager/piechart', views.pie_chart, name='piechart'),
    path('manager/barchart', views.bar_chart, name='barchart'),
    path('manager/linechart', views.line_chart, name='linechart'),
    path('manager/', views.switch_mng, name='mng'),
    path('employee/', views.switch_emp, name='emp'),
]