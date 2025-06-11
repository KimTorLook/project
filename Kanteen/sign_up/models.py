from django.db import models

# Create your models here.
class Student_profile(models.Model):
    student_id = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    email = models.EmailField(unique=True)
    school_id = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.email