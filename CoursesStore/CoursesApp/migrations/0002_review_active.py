# Generated by Django 4.0.4 on 2022-06-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
