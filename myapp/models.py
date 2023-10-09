from django.db import models

class Course(models.Model):
  name = models.CharField(max_length=255)
  credit_hour = models.IntegerField()

  def __str__(self):
    return self.name

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=255)
  level = models.IntegerField()
  roll_no = models.IntegerField()
  study_hours = models.IntegerField(default=0)
  courses = models.ManyToManyField(Course)
  age = models.IntegerField()
  phone_no = models.CharField(max_length=15)
  year_joined = models.CharField(max_length=5)

  def __str__(self):
    return self.name
  

class Teacher(models.Model):
  name = models.CharField(max_length=255)
  courses = models.ManyToManyField(Course)
  age = models.IntegerField()
  phone_no = models.CharField(max_length=15)
  year_joined = models.CharField(max_length=5)

  def __str__(self):
    return self.name
