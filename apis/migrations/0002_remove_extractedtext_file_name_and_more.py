# Generated by Django 5.1.3 on 2025-01-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extractedtext',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='extractedtext',
            name='text_content',
        ),
        migrations.AddField(
            model_name='extractedtext',
            name='file_name1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extractedtext',
            name='file_name2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extractedtext',
            name='file_name3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extractedtext',
            name='text_content1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extractedtext',
            name='text_content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extractedtext',
            name='text_content3',
            field=models.TextField(blank=True, null=True),
        ),
    ]