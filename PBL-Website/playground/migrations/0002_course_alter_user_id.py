# Generated by Django 5.1.4 on 2025-01-18 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=50, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('section_a_model_answer', models.FileField(upload_to='model_answers/section_a/')),
                ('section_b_model_answer', models.FileField(upload_to='model_answers/section_b/')),
                ('section_c_model_answer', models.FileField(upload_to='model_answers/section_c/')),
                ('max_marks_a', models.PositiveIntegerField()),
                ('max_marks_b', models.PositiveIntegerField()),
                ('max_marks_c', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
