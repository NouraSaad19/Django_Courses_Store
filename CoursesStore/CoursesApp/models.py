from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    duration = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="courses/images/")
    online = models.BooleanField()
    start_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta: #the price of the courses order from highest to lowest
        ordering=('-price',)
    def get_absolute_url(self):
        return '/detail/{}'.format(self.pk)


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='review')
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"]])
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment


class Order(models.Model):
    order = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    totalprice = models.IntegerField()