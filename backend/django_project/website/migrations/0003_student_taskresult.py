# Generated by Django 3.1.2 on 2020-10-31 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_task_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskResults', to='website.student')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskResults', to='website.task')),
            ],
        ),
    ]