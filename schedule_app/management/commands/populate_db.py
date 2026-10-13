from datetime import time
from django.core.management.base import BaseCommand
from schedule_app.models import Subject, Teacher, Lesson

class Command(BaseCommand):
    def handle(self, *args, **options):
        Lesson.objects.all().delete()
        Teacher.objects.all().delete()
        Subject.objects.all().delete()

        sub_physics = Subject.objects.create(name='Physics I')
        sub_mechanics = Subject.objects.create(name='Mechanics')
        sub_math = Subject.objects.create(name='Math')
        sub_history = Subject.objects.create(name='History')

        t_smith = Teacher.objects.create(name='Dr. Smith', email='smith@university.edu')
        t_smith.subjects.add(sub_physics, sub_mechanics)

        t_food = Teacher.objects.create(name='Dr. Si. Food', email='sifood@university.edu')
        t_food.subjects.add(sub_physics, sub_mechanics, sub_history)

        t_miller = Teacher.objects.create(name='Dr. Miller', email='miller@university.edu')
        t_miller.subjects.add(sub_physics, sub_math)

        t_hashow = Teacher.objects.create(name='Dr. Hashow', email='hashow@university.edu')
        t_hashow.subjects.add(sub_physics, sub_mechanics, sub_math)

        schedule_data = [
            {
                'day': 'monday', 'pair': 1, 'start': time(8, 30), 'end': time(10, 0),
                'sub': sub_physics, 't': t_smith, 'room': '301B',
                'notes': 'Introduction to Mechanics. Chapter 1. Please prepare questions.',
                'cancelled': False
            },
            {
                'day': 'monday', 'pair': 2, 'start': time(10, 15), 'end': time(11, 45),
                'sub': sub_math, 't': t_miller, 'room': '204',
                'notes': 'Class cancelled due to department conference.',
                'cancelled': True
            },
            {
                'day': 'monday', 'pair': 3, 'start': time(11, 0), 'end': time(12, 30),
                'sub': sub_physics, 't': t_smith, 'room': '301B',
                'notes': 'Laboratory work in building B.',
                'cancelled': False
            },
            {
                'day': 'monday', 'pair': 4, 'start': time(13, 15), 'end': time(14, 45),
                'sub': sub_physics, 't': t_smith, 'room': '301B',
                'notes': 'Discussion on kinematics and dynamics.',
                'cancelled': False
            },

            {
                'day': 'tuesday', 'pair': 1, 'start': time(8, 30), 'end': time(10, 0),
                'sub': sub_physics, 't': t_smith, 'room': '301B',
                'notes': 'Electrostatics theory review.',
                'cancelled': False
            },
            {
                'day': 'tuesday', 'pair': 2, 'start': time(10, 15), 'end': time(11, 45),
                'sub': sub_history, 't': t_food, 'room': '105',
                'notes': 'Ancient world civilizations.',
                'cancelled': False
            },
            {
                'day': 'tuesday', 'pair': 3, 'start': time(11, 0), 'end': time(12, 30),
                'sub': sub_history, 't': t_food, 'room': '105',
                'notes': 'European Renaissance culture.',
                'cancelled': False
            },
            {
                'day': 'tuesday', 'pair': 4, 'start': time(13, 15), 'end': time(14, 45),
                'sub': sub_history, 't': t_food, 'room': '105',
                'notes': 'Modern history seminar.',
                'cancelled': False
            },

            {
                'day': 'wednesday', 'pair': 1, 'start': time(8, 30), 'end': time(10, 0),
                'sub': sub_physics, 't': t_smith, 'room': '301B',
                'notes': 'Thermodynamics overview.',
                'cancelled': False
            },
            {
                'day': 'wednesday', 'pair': 2, 'start': time(10, 15), 'end': time(11, 45),
                'sub': sub_mechanics, 't': t_hashow, 'room': '210',
                'notes': 'Fluid mechanics experiments.',
                'cancelled': False
            },
            {
                'day': 'wednesday', 'pair': 3, 'start': time(11, 0), 'end': time(12, 30),
                'sub': sub_mechanics, 't': t_hashow, 'room': '210',
                'notes': 'Hydrodynamics calculations.',
                'cancelled': False
            },
            {
                'day': 'wednesday', 'pair': 4, 'start': time(13, 15), 'end': time(14, 45),
                'sub': sub_history, 't': t_food, 'room': '105',
                'notes': 'Source analysis workshop.',
                'cancelled': False
            },

            {
                'day': 'thursday', 'pair': 1, 'start': time(8, 30), 'end': time(10, 0),
                'sub': sub_math, 't': t_miller, 'room': '204',
                'notes': 'Cancelled by dean office.',
                'cancelled': True
            },
            {
                'day': 'thursday', 'pair': 2, 'start': time(10, 15), 'end': time(11, 45),
                'sub': sub_math, 't': t_miller, 'room': '204',
                'notes': 'Cancelled by dean office.',
                'cancelled': True
            },
            {
                'day': 'thursday', 'pair': 3, 'start': time(11, 0), 'end': time(12, 30),
                'sub': sub_physics, 't': t_hashow, 'room': '210',
                'notes': 'Quantum mechanics foundations.',
                'cancelled': False
            },
            {
                'day': 'thursday', 'pair': 4, 'start': time(13, 15), 'end': time(14, 45),
                'sub': sub_physics, 't': t_hashow, 'room': '210',
                'notes': 'Problem solving session.',
                'cancelled': False
            },

            {
                'day': 'friday', 'pair': 1, 'start': time(8, 30), 'end': time(10, 0),
                'sub': sub_physics, 't': t_smith, 'room': '301B',
                'notes': 'Optics and photonics.',
                'cancelled': False
            },
            {
                'day': 'friday', 'pair': 2, 'start': time(10, 15), 'end': time(11, 45),
                'sub': sub_history, 't': t_food, 'room': '105',
                'notes': 'Oral presentations.',
                'cancelled': False
            },
            {
                'day': 'friday', 'pair': 3, 'start': time(11, 0), 'end': time(12, 30),
                'sub': sub_physics, 't': t_hashow, 'room': '210',
                'notes': 'Electromagnetism seminar.',
                'cancelled': False
            },
            {
                'day': 'friday', 'pair': 4, 'start': time(13, 15), 'end': time(14, 45),
                'sub': sub_history, 't': t_food, 'room': '105',
                'notes': 'Weekly recap and quiz.',
                'cancelled': False
            },
        ]

        for item in schedule_data:
            Lesson.objects.create(
                day_of_week=item['day'],
                pair_number=item['pair'],
                start_time=item['start'],
                end_time=item['end'],
                subject=item['sub'],
                teacher=item['t'],
                classroom=item['room'],
                notes=item['notes'],
                is_cancelled=item['cancelled'],
                group_name='GROUP 2024-A'
            )

        self.stdout.write('Database populated successfully.')
