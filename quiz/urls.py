from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_request/', views.login_request, name='login_request'),
    path('questions/<int:student_id>/', views.questions, name='questions'),
    path('detail/<int:question_id>/<int:student_id>/', views.detail, name='detail'),
    path('checkAns/<int:question_id>/<int:student_id>/', views.checkAns, name='checkAns'),
    path('<int:student_id>/submit/', views.submit, name='submit'),
    # path('<int:question_id>/submit/', views.submit, name='submit'),
]