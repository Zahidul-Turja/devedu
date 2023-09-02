# Generated by Django 4.1.4 on 2023-08-29 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("devedu", "0026_remove_coursesession_course_coursesession_course"),
    ]

    operations = [
        migrations.RemoveField(model_name="coursesession", name="course",),
        migrations.CreateModel(
            name="CourseSessionMiddle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sessions",
                        to="devedu.course",
                    ),
                ),
                (
                    "sessions",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="session",
                        to="devedu.coursesession",
                    ),
                ),
            ],
        ),
    ]
