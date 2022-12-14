# Generated by Django 4.1.2 on 2022-11-14 09:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200, null=True, verbose_name='Полученная специальность')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_begin', models.DateField(max_length=200, null=True, verbose_name='Начало обучения')),
                ('education_end', models.DateField(max_length=200, null=True, verbose_name='Окончание обучения')),
                ('educational_institution_name', models.CharField(max_length=200, null=True, verbose_name='Название организации')),
                ('faculty', models.CharField(max_length=200, null=True, verbose_name='Факультет')),
                ('speciality', models.CharField(max_length=200, null=True, verbose_name='Полученная специальность')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_begin', models.DateField(max_length=200, null=True, verbose_name='Начало работы')),
                ('work_end', models.DateField(max_length=200, null=True, verbose_name='Окончание работы')),
                ('company', models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(0)], verbose_name='Название организации')),
                ('job_title', models.CharField(max_length=200, null=True, verbose_name='Должность')),
                ('responsibilities', models.TextField(max_length=3000, null=True, verbose_name='Рабочие обязанности')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_name', models.CharField(max_length=100, null=True, verbose_name='Профессия')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200, null=True, verbose_name='Должность')),
                ('salary_level', models.FloatField(null=True, verbose_name='Уровень зарплаты')),
                ('about_user', models.TextField(max_length=3000, null=True, verbose_name='Информация о себе')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Электронная почта')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('telegram_link', models.CharField(max_length=200, null=True, verbose_name='Telegram')),
                ('linkedin_link', models.CharField(max_length=200, null=True, verbose_name='Linkedin')),
                ('facebook_link', models.CharField(max_length=200, null=True, verbose_name='Facebook')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('courses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='resumes.course', verbose_name='Курсы')),
                ('educational_institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='resumes.education', verbose_name='Учебное заведение')),
                ('place_of_work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='resumes.experience', verbose_name='Место работы')),
                ('profession', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='resumes.profession', validators=[django.core.validators.MinLengthValidator(0)], verbose_name='Профессия')),
            ],
        ),
    ]
