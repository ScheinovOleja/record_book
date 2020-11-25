from django.shortcuts import render

# Create your views here.
from django.views import View, generic

from first_page.models import StudentBook, StudentInfo, UserProfile


def login(request):
    return render(request, 'login.html', {})


class Index(generic.View):

    def __init__(self):
        super().__init__()
        self.userprofile = UserProfile.objects.all()
        self.template_name = 'index.html'
        self.context_object_name = 'student'
        self.queryset = StudentBook.objects.all()

    def get(self, request):
        for e in self.userprofile:
            return render(request, self.template_name, {self.context_object_name: self.queryset, 'userprofile': e})


class AssessmentsInfo(generic.View):

    def __init__(self):
        super().__init__()
        self.model = StudentBook
        self.template_name = 'assessments.html'
        self.context_object_name = 'assessments'

    def get(self, request, reg_num):
        context = StudentBook.objects.filter(student__education_activity__reg_num=reg_num)
        for content in context:
            return render(request, self.template_name, {self.context_object_name: content})


class StudentsInfo(generic.View):

    def __init__(self):
        super().__init__()
        self.model = StudentInfo
        self.template_name = 'students.html'
        self.context_object_name = 'information'

    def get(self, request, reg_num):
        context = StudentInfo.objects.filter(education_activity__reg_num=reg_num)
        for content in context:
            return render(request, self.template_name, {self.context_object_name: content})
