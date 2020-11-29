from django.urls import path, include
from django.contrib.auth import views as views
from . import views as view

urlpatterns = [
    path('', view.Index.as_view(), name='first_page'),
    path('info/<str:reg_num>', view.AssessmentsInfo.as_view(), name='info'),
    path('student/<str:reg_num>', view.StudentsInfo.as_view(), name='student'),
    path('teacher/', view.TeachersInfo.as_view(), name='teacher'),
    path('teacher/<int:pk>', view.TeacherDetail.as_view(), name='teacher_detail')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
