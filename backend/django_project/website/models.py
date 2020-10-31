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
    url = models.SlugField(max_length=130, unique=True, default=0)

    def __str__(self):
        return self.title


class Class(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey('Teacher', related_name='classes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    #Class = models.ForeignKey('Class', related_name="students", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TaskResult(models.Model):
    task = models.ForeignKey('Task', related_name='taskResults', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', related_name='taskResults', on_delete=models.CASCADE)
    mark = models.FloatField()


class CodeReview(models.Model):
    comment = models.TextField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)

