from django.contrib import admin

from .models import Teacher, Task, Student, TaskResult

admin.site.register(Teacher)
admin.site.register(Task)
admin.site.register(TaskResult)
admin.site.register(Student)

