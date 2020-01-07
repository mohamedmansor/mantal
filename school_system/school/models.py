from django.db import models


class School(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
