# Generated by Django 4.1.4 on 2023-07-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devedu", "0012_userprofile_github_userprofile_linkedin_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="first_name",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
