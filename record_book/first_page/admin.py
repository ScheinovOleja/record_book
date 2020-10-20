from django.contrib import admin

# Register your models here.
from first_page.models import StudentBook, StudentInfo, AssessmentInfo, ControlInfo, TeacherInfo, DisciplineInfo


@admin.register(StudentBook, StudentInfo, AssessmentInfo, ControlInfo, TeacherInfo, DisciplineInfo)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
