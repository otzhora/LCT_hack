from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=120)
    task = models.TextField()
    path = models.TextField()
    teacher = models.ForeignKey('Teacher', related_name='tasks', on_delete=models.CASCADE)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title
