# Generated by Django 5.0.3 on 2024-04-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('fees', models.PositiveIntegerField()),
            ],
        ),
    ]
