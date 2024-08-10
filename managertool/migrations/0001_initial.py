# Generated by Django 4.0.6 on 2023-02-09 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='project name')),
                ('description', models.TextField()),
                ('executors', models.IntegerField()),
                ('deadline', models.DateField(help_text='YYYY-MM-DD')),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('executiontime', models.IntegerField(help_text='Hour(s)', verbose_name='execution time')),
                ('created', models.DateField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managertool.project')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
