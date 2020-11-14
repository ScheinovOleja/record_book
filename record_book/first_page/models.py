from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.


class StudentBook(models.Model):
    student = models.ForeignKey('StudentInfo', null=True, on_delete=models.CASCADE,
                                verbose_name='Студент')
    semester = models.IntegerField(default=0, verbose_name='Семестр')
    discipline = models.ForeignKey('DisciplineInfo', null=True, on_delete=models.CASCADE,
                                   verbose_name='Дисциплина')
    teacher = models.ForeignKey('TeacherInfo', null=True, on_delete=models.CASCADE,
                                verbose_name='Учитель')
    control = models.ForeignKey('ControlInfo', null=True, on_delete=models.CASCADE,
                                verbose_name='Вид контроля')
    assessment = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return f'{str(self.student)} - {str(self.discipline)}'


class StudentInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class DisciplineInfo(models.Model):
    discipline = models.CharField(default='', max_length=50, verbose_name='Дисциплина')

    def __str__(self):
        return self.discipline


class TeacherInfo(models.Model):
    name = models.CharField(default='', max_length=30, verbose_name='Имя')
    surname = models.CharField(default='', max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(default='', max_length=30, verbose_name='Отчество')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class ControlInfo(models.Model):
    control = models.CharField(max_length=10, default=True, verbose_name='Зачет/Экзамен')

    def __str__(self):
        return self.control
