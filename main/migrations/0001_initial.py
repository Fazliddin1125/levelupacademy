# Generated by Django 4.2.7 on 2023-11-13 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('month', models.FloatField()),
                ('price', models.FloatField()),
                ('student', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('checked', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.course')),
            ],
        ),
    ]