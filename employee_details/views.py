from django.shortcuts import render, redirect
from .forms import EmployeeRegForm
from django.contrib import messages
from .models import Employee

def list_of_employee(request):
    employees = Employee.objects.all()
    return render(request, 'employee_details/employee_list.html', {'employees': employees})

def employee_reg_form(request, id=0):
        if request.method == 'GET':
            if id == 0:
                # insert operation for id=0
                form = EmployeeRegForm()
            else:
                # insert operation for id =1,2,3, etc
                employee = Employee.objects.get(pk=id)
                form = EmployeeRegForm(instance=employee)
            return render(request, 'employee_details/employee_form.html', {'form': form})
        else:
            if id == 0:
                form = EmployeeRegForm(request.POST)
            else:
                employee = Employee.objects.get(pk=id)
                form = EmployeeRegForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                messages.success(request, f'Form is successful')
            return redirect('employee_list')


def employee_delete(request, id):
    delete_employee = Employee.objects.get(pk=id).delete()
    return redirect('employee_list')