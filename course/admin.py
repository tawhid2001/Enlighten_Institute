from django.contrib import admin
from . import models

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('course_name',),}
admin.site.register(models.Course,CourseAdmin)
admin.site.register(models.Lesson)
