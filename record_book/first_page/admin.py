from django.contrib import admin

# Register your models here.
from first_page.models import StudentBook, StudentInfo, ControlInfo, TeacherInfo, DisciplineInfo


@admin.register(StudentBook, StudentInfo, ControlInfo, TeacherInfo, DisciplineInfo)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
