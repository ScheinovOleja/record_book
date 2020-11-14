from django.shortcuts import render


# Create your views here.
from django.views import View, generic

from first_page.models import StudentBook, StudentInfo


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def test(request):
    return render(request, 'students.html', {})


class ViewInfo(generic.ListView):
    model = StudentBook
    template_name = 'assessments.html'
    context_object_name = 'advertisement_list'
    queryset = StudentBook.objects.all()


class StudentsInfo(generic.ListView):
    model = StudentInfo
    template_name = 'students.html'
    context_object_name = 'information'
    queryset = StudentInfo.objects.all()
