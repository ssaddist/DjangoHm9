from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def lessons_count(self):
        return self.lessons.count()

class Lesson(models.Model):
    DAY_CHOICES = (
        ('monday', 'Понеділок'),
        ('tuesday', 'Вівторок'),
        ('wednesday', 'Середа'),
        ('thursday', 'Четвер'),
        ('friday', 'Пʼятниця'),
        ('saturday', 'Субота'),
        ('sunday', 'Неділя'),
    )

    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES)
    pair_number = models.PositiveSmallIntegerField(default=1)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    classroom = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    is_cancelled = models.BooleanField(default=False)
    group_name = models.CharField(max_length=50, default='GROUP 2024-A')

    class Meta:
        ordering = ['day_of_week', 'pair_number', 'start_time']

    def __str__(self):
        return f"{self.subject.name} - {self.get_day_of_week_display()}"
