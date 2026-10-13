from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Subject, Teacher, Lesson

DAYS_MAP = {
    'monday': {'key': 'monday', 'name': 'Monday', 'ua_name': 'Понеділок', 'short': 'MON'},
    'tuesday': {'key': 'tuesday', 'name': 'Tuesday', 'ua_name': 'Вівторок', 'short': 'TUE'},
    'wednesday': {'key': 'wednesday', 'name': 'Wednesday', 'ua_name': 'Середа', 'short': 'WED'},
    'thursday': {'key': 'thursday', 'name': 'Thursday', 'ua_name': 'Четвер', 'short': 'THU'},
    'friday': {'key': 'friday', 'name': 'Friday', 'ua_name': 'Пʼятниця', 'short': 'FRI'},
    'saturday': {'key': 'saturday', 'name': 'Saturday', 'ua_name': 'Субота', 'short': 'SAT'},
    'sunday': {'key': 'sunday', 'name': 'Sunday', 'ua_name': 'Неділя', 'short': 'SUN'},
}

def get_base_context(active_day=None):
    return {
        'group_name': 'GROUP 2024-A',
        'current_week': 'WEEK: 16 (Current)',
        'days_list': list(DAYS_MAP.values()),
        'active_day': active_day,
    }

def home_view(request):
    context = get_base_context(active_day='monday')
    return render(request, 'schedule/home.html', context)

def week_schedule_view(request):
    time_slots_def = [
        {'pair_number': 1, 'time_label': '08:30'},
        {'pair_number': 2, 'time_label': '10:15'},
        {'pair_number': 3, 'time_label': '11:00'},
        {'pair_number': 4, 'time_label': '13:15'},
    ]
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    
    all_lessons = Lesson.objects.select_related('subject', 'teacher').all()
    lesson_matrix = {}
    for lesson in all_lessons:
        lesson_matrix[(lesson.day_of_week, lesson.pair_number)] = lesson

    rows = []
    for slot in time_slots_def:
        row_cells = []
        for day_key in week_days:
            lesson = lesson_matrix.get((day_key, slot['pair_number']))
            row_cells.append({
                'day': day_key,
                'lesson': lesson
            })
        rows.append({
            'time_label': slot['time_label'],
            'cells': row_cells
        })

    context = get_base_context()
    context.update({
        'table_days': [DAYS_MAP[d] for d in week_days],
        'rows': rows,
    })
    return render(request, 'schedule/week.html', context)

def day_schedule_view(request, day):
    day_key = day.lower()
    if day_key not in DAYS_MAP:
        raise Http404(f"День '{day}' не знайдено.")

    day_info = DAYS_MAP[day_key]
    lessons = Lesson.objects.filter(day_of_week=day_key).select_related('subject', 'teacher').order_by('pair_number', 'start_time')

    context = get_base_context(active_day=day_key)
    context.update({
        'day_info': day_info,
        'lessons': lessons,
    })
    return render(request, 'schedule/day.html', context)

def lesson_detail_view(request, pk):
    lesson = get_object_or_404(Lesson.objects.select_related('subject', 'teacher'), pk=pk)
    context = get_base_context(active_day=lesson.day_of_week)
    context['lesson'] = lesson
    return render(request, 'schedule/detail.html', context)

def teachers_view(request):
    teachers = Teacher.objects.prefetch_related('subjects', 'lessons').all()
    context = get_base_context()
    context['teachers'] = teachers
    return render(request, 'schedule/teachers.html', context)
