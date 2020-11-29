from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.

from first_page.models import StudentBook, StudentInfo, ControlInfo, Teacher, Discipline, EducationalActivities


@admin.register(StudentBook, StudentInfo, ControlInfo, Teacher, Discipline, EducationalActivities)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
