# Generated by Django 5.2.1 on 2025-06-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0021_student_user_alter_order_confirm_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
