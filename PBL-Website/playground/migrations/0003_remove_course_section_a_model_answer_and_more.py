# Generated by Django 5.1.4 on 2025-01-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_course_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='section_a_model_answer',
        ),
        migrations.RemoveField(
            model_name='course',
            name='section_b_model_answer',
        ),
        migrations.RemoveField(
            model_name='course',
            name='section_c_model_answer',
        ),
        migrations.AddField(
            model_name='course',
            name='section_a_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='section_b_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='section_c_text',
            field=models.TextField(default=''),
        ),
    ]