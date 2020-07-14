
from django import forms
from .models import Employee, Position

class EmployeeRegForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname', 'mobile', 'emp_code',  'position']
        labels = {
            'fullname': 'FullName ',
            'emp_code': 'EMP.Code',
        }

    # just like a widget in normal form or a placeholder in our html
    def __init__(self, *args, **kwargs):
        super(EmployeeRegForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'select'
        # # to remove required validation from a form input e.g
        # self.fields['title'].required = False

class EmployeePositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(EmployeePositionForm, self).__init__(*args, **kwargs)
        self.fields['title'].required= False