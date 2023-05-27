from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    price = models.CharField(max_length=16, verbose_name='Цена курса')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя учителя')
    salary = models.CharField(max_length=8, verbose_name='Зарплата')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя студента')
    courses = models.ManyToManyField(Course)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name