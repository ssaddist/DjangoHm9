from django.test import TestCase, Client
from django.urls import reverse
from schedule_app.models import Subject, Teacher, Lesson
from datetime import time

class ScheduleViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.subject = Subject.objects.create(name='Physics I')
        self.subject_math = Subject.objects.create(name='Math')
        self.teacher = Teacher.objects.create(name='Dr. Smith', email='smith@uni.edu')
        self.teacher.subjects.add(self.subject, self.subject_math)
        
        self.lesson_active = Lesson.objects.create(
            day_of_week='monday',
            pair_number=1,
            start_time=time(8, 30),
            end_time=time(10, 0),
            subject=self.subject,
            teacher=self.teacher,
            classroom='301B',
            notes='Introductory lecture.',
            is_cancelled=False
        )
        self.lesson_cancelled = Lesson.objects.create(
            day_of_week='monday',
            pair_number=2,
            start_time=time(10, 15),
            end_time=time(11, 45),
            subject=self.subject_math,
            teacher=self.teacher,
            classroom='204',
            notes='Cancelled class.',
            is_cancelled=True
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'GROUP 2024-A')
        self.assertContains(response, 'WEEK: 16 (Current)')
        self.assertContains(response, 'View Full Week')
        self.assertContains(response, 'Find Teachers')
        self.assertContains(response, 'Quick Look')

    def test_week_schedule_page(self):
        response = self.client.get(reverse('week_schedule'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Weekly Schedule')
        self.assertContains(response, 'Physics I')
        self.assertContains(response, 'CANCELLED')
        self.assertContains(response, '1. 08:30')

    def test_day_schedule_valid(self):
        response = self.client.get(reverse('day_schedule', args=['monday']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'MONDAY')
        self.assertContains(response, 'Physics I')
        self.assertContains(response, 'CANCELLED')

    def test_day_schedule_invalid_day_returns_404(self):
        response = self.client.get('/schedule/notaday/')
        self.assertEqual(response.status_code, 404)

    def test_day_schedule_weekend_empty(self):
        response = self.client.get(reverse('day_schedule', args=['sunday']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Вихідний')

    def test_lesson_detail(self):
        response = self.client.get(reverse('lesson_detail', args=[self.lesson_active.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Physics I')
        self.assertContains(response, 'Dr. Smith')
        self.assertContains(response, '301B')
        self.assertContains(response, '08:30 - 10:00')
        self.assertContains(response, 'Introductory lecture.')

    def test_teachers_page(self):
        response = self.client.get(reverse('teachers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dr. Smith')
        self.assertContains(response, 'Math, Physics I')
        self.assertContains(response, '2 classes')
