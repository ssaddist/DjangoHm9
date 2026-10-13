
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('subjects', models.ManyToManyField(blank=True, related_name='teachers', to='schedule_app.subject')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('monday', 'Понеділок'), ('tuesday', 'Вівторок'), ('wednesday', 'Середа'), ('thursday', 'Четвер'), ('friday', 'Пʼятниця'), ('saturday', 'Субота'), ('sunday', 'Неділя')], max_length=20)),
                ('pair_number', models.PositiveSmallIntegerField(default=1)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('classroom', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('group_name', models.CharField(default='GROUP 2024-A', max_length=50)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='schedule_app.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='schedule_app.teacher')),
            ],
            options={
                'ordering': ['day_of_week', 'pair_number', 'start_time'],
            },
        ),
    ]
