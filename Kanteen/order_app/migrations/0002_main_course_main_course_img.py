# Generated by Django 5.1.4 on 2025-06-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_course',
            name='main_course_img',
            field=models.ImageField(null=True, upload_to='project'),
        ),
    ]
