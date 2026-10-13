from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('index/', views.home_view, name='index'),
    path('schedule/', views.week_schedule_view, name='week_schedule'),
    path('schedule/lesson/<int:pk>/', views.lesson_detail_view, name='lesson_detail'),
    path('schedule/<int:pk>/', views.lesson_detail_view, name='lesson_detail_pk'),
    path('schedule/<str:day>/', views.day_schedule_view, name='day_schedule'),
    path('teachers/', views.teachers_view, name='teachers'),
]
