from django.urls import path
from . import views

urlpatterns = [
    # post request for the insert operation
    path('', views.employee_reg_form, name='employee_insert'),
    # get and post request for the update operation
    path('list/<int:id>/', views.employee_reg_form, name='employee_update'),
    # select all records from the database
    path('list/', views.list_of_employee, name='employee_list'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
]