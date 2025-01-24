# Generated by Django 5.1.3 on 2025-01-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_studentanswer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='max_marks_a',
            new_name='max_marks_section_a',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='max_marks_b',
            new_name='max_marks_section_b',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='max_marks_c',
            new_name='max_marks_section_c',
        ),
        migrations.RemoveField(
            model_name='course',
            name='section_a_text',
        ),
        migrations.RemoveField(
            model_name='course',
            name='section_b_text',
        ),
        migrations.RemoveField(
            model_name='course',
            name='section_c_text',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]