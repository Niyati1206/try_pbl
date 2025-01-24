# Generated by Django 5.1.3 on 2025-01-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_rename_max_marks_a_course_max_marks_section_a_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='extracted_text_a',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='extracted_text_b',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='extracted_text_c',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='roll_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='section_a_answer',
            field=models.FileField(upload_to='student_answers/section_a/'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='section_b_answer',
            field=models.FileField(upload_to='student_answers/section_b/'),
        ),
        migrations.AlterField(
            model_name='studentanswer',
            name='section_c_answer',
            field=models.FileField(upload_to='student_answers/section_c/'),
        ),
    ]
