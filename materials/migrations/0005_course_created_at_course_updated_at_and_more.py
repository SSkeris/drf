# Generated by Django 4.2.2 on 2024-07-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0004_course_amount_lesson_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="дата создания"
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="дата создания"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="дата обновления"
            ),
        ),
    ]
