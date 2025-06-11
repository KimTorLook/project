from django import forms
from .models import Student_profile

class Student_profileForm(forms.ModelForm):
    class Meta:
        model = Student_profile
        fields = ['student_id', 'first_name', 'last_name', 'date_of_birth', 'email', 'school_id']


