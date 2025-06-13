from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import uuid

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
    school_address = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.school_name
    

class Student(models.Model):
    stid = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True, unique=True)
    is_active=models.BooleanField(blank=False, null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.restaurant_name

class Main_Course(models.Model): # main course menu
    main_course_id = models.AutoField(primary_key=True)
    main_course_name = models.CharField(max_length=150, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    main_course_cost = models.IntegerField(blank=True, null=True, default=20)
    main_course_price = models.IntegerField(blank=True, null=True, default=60)
    main_course_img = models.ImageField("Image", upload_to="main_course", null=True)
    #<img src="{% static ' order_app/main_course_img.jpeg' %}" alt="">

    def __str__(self):
        return self.main_course_name
    
 

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_date_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    meal1 = models.ForeignKey(Main_Course, on_delete=models.CASCADE, related_name="meal1", blank=True, null=True, default="叉燒蛋飯")
    meal3 = models.ForeignKey(Main_Course, on_delete=models.CASCADE, related_name="meal3", blank=True, null=True, default="叉燒蛋飯")
    meal2 = models.ForeignKey(Main_Course, on_delete=models.CASCADE, related_name="meal2", blank=True, null=True, default="叉燒蛋飯")
    meal4 = models.ForeignKey(Main_Course, on_delete=models.CASCADE, related_name="meal4", blank=True, null=True, default="叉燒蛋飯")
    meal5 = models.ForeignKey(Main_Course, on_delete=models.CASCADE, related_name="meal5", blank=True, null=True, default="叉燒蛋飯")
    total_price = models.IntegerField(blank=True, null=True, default=300)
    payment_method = models.CharField(max_length=50, blank=True, null=True, default="Payme")
    confirm_payment = models.BooleanField(blank=True, null=True)

    def calculate_total_price(self):
        meals = [self.meal1, self.meal2, self.meal3, self.meal4, self.meal5]
        total = 0
        for meal in meals:
            if meal and meal.main_course_price: 
                total += meal.main_course_price if meal.main_course_price is not None else 0
        return total

    def save(self):
        self.total_price = self.calculate_total_price()
        super().save()

    def __str__(self):
        return f"{self.order_id} - {self.order_date_time}"
    
