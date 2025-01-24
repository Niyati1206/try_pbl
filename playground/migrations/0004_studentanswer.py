# Generated by Django 5.1.4 on 2025-01-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_remove_course_section_a_model_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=50)),
                ('roll_number', models.PositiveIntegerField()),
                ('student_name', models.CharField(max_length=100)),
                ('section_a_answer', models.FileField(upload_to='answers/section_a/')),
                ('section_b_answer', models.FileField(upload_to='answers/section_b/')),
                ('section_c_answer', models.FileField(upload_to='answers/section_c/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]