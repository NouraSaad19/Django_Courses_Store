# Generated by Django 4.0.4 on 2022-06-04 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0006_alter_course_options_review_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='active',
        ),
    ]
