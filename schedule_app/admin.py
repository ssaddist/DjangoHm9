from django.contrib import admin
from .models import Subject, Teacher, Lesson

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    filter_horizontal = ('subjects',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'day_of_week', 'pair_number', 'start_time', 'end_time', 'classroom', 'is_cancelled')
    list_filter = ('day_of_week', 'is_cancelled', 'teacher')
    search_fields = ('subject__name', 'teacher__name', 'classroom', 'notes')
