from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class School(models.Model):
    class SchoolName(models.TextChoices):
        SPCC = "SPCC", _("St. Paul's Co-educational College")
        DGS = "DGS", _("Diocesan Girls' School")
        HY = "HY", _("Heep Yunn School")
        SMCC = "SMCC", _("St. Mary's Canossian College")
        MCS = "MCS", _("Maryknoll Convent School(Secondary Section)")
        SPCS = "SPCS", _("St. Paul's Convent School")
        LSC = "LSC", _("La Salle College")
        QC = "QC", _("Queen's College")
        HKTATH = "HKTATH", _("Hong Kong Taoist Association Tang Hin Memorial Secondary School")
        SKHTST = "SKHTST", _(" S.K.H. Tsang Shiu Tim Secondary School")

    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(
        max_length=10,
        choices=SchoolName.choices,
        default=SchoolName.SPCC)
    school_address = models.TextField(max_length=300)

    def __str__(self):
        return self.school_name
    

class Student(models.Model):
    stid = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=20, editable=False)
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateTimeField(auto_now=False)
    Email = models.EmailField(blank=False, unique=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    is_active=models.BooleanField(blank=False, null=False)
    
    def __str__(self):
        return self.stid

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.TextField()

    def __str__(self):
        return self.restaurant_id

class Main_Course(models.Model):
    main_course_id = models.AutoField(primary_key=True)
    main_course_name = models.CharField(max_length=150)
    main_course_cost = models.IntegerField()
    main_course_price = models.IntegerField()

    def __str__(self):
        return self.main_course_id

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True)
    order_date_time = models.DateTimeField(auto_now=False)
    payment_method = models.CharField(max_length=50)
    confirm_payment = models.BooleanField()
    meals = models.ManyToManyField(Main_Course)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)

    def get_choose(self):
        return json.loads(self.choose)
    
    def set_choose(self):
        self.choose = json.dumps(meal_)

    def __str__(self):
        return self.order_id

    def load_menu(self):
        pass
        #menu_list = list_of_menu

"""class Set_Menu(models.Model):
    menu_id = models.AutoField(primary_key=True, default=0)
    main_course_id = models.ForeignKey(Main_Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant_id
"""
