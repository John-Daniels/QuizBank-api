# Generated by Django 4.0 on 2022-07-15 20:19

from django.db import migrations, models
import django.db.models.deletion
import quiz.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], db_index=True, max_length=100)),
                ('type', models.CharField(choices=[('multiple-choice', 'Multiple Choice'), ('True / False', 'True / False')], db_index=True, max_length=100)),
                ('correct_answer', models.CharField(max_length=200)),
                ('explanation', models.CharField(blank=True, max_length=1000)),
                ('is_verified', models.BooleanField(default=False)),
                ('date_verified', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='quiz/')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('category', models.ForeignKey(on_delete=models.SET(quiz.models.get_sentinel_category), related_name='questions', to='quiz.category')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='authentication.user')),
                ('verified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions_verified', to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='InCorrectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=1000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incorrect_answers', to='quiz.question')),
            ],
        ),
    ]
