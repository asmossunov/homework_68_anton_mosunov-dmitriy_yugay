# Generated by Django 4.1.2 on 2022-11-14 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0003_remove_resume_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='resumes.profession', verbose_name='Профессия'),
        ),
    ]
