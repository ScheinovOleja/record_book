from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from record_book import settings


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_num = models.CharField(max_length=30, verbose_name='Регистрационный номер')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class StudentBook(models.Model):
    student = models.ForeignKey('StudentInfo', null=True, on_delete=models.CASCADE,
                                verbose_name='Студент')
    semester = models.IntegerField(default=0, verbose_name='Семестр')
    discipline = models.ForeignKey('DisciplineInfo', null=True, on_delete=models.CASCADE,
                                   verbose_name='Дисциплина')
    date = models.DateField(verbose_name='Дата экзамена/зачета', default=datetime.now)
    teacher = models.ForeignKey('TeacherInfo', null=True, on_delete=models.CASCADE,
                                verbose_name='Учитель')
    control = models.ForeignKey('ControlInfo', null=True, on_delete=models.CASCADE,
                                verbose_name='Вид контроля')
    assessment = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        verbose_name='Оценка'
    )

    def __str__(self):
        return f'{str(self.student)} - {str(self.discipline)}'


class EducationalActivities(models.Model):
    reg_num = models.CharField(max_length=30, verbose_name='Регистрационный номер')
    status = models.CharField(max_length=30, verbose_name='Статус')
    category = models.CharField(max_length=30, verbose_name='Категория зачисления')
    institute = models.CharField(max_length=150, verbose_name='Институт')
    direction = models.CharField(max_length=150, verbose_name='Направление подготовки')
    forms_study = models.CharField(max_length=30, verbose_name='Форма обучения')
    course = models.IntegerField(verbose_name='Курс', default=1)
    group = models.IntegerField(verbose_name='Группа', default=1)
    scholarship = models.BooleanField(verbose_name='Стипендия', default=True)

    def __str__(self):
        return f"{self.reg_num}"


class StudentInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения', default=None)
    sex = models.BooleanField(verbose_name='М/Ж', default=True)
    military = models.BooleanField(verbose_name='Отношение к воинской службе', default=True)
    education_activity = models.ForeignKey('EducationalActivities', verbose_name='Номер зачетки',
                                           on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email', default=None)

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
    control = models.CharField(max_length=10, default='', verbose_name='Зачет/Экзамен')

    def __str__(self):
        return self.control
