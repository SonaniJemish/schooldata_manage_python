# Generated by Django 4.2.8 on 2024-01-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studentapp", "0007_rename_sjoindatw_student_sjoindate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student", name="sjoindate", field=models.DateField(blank=True),
        ),
    ]