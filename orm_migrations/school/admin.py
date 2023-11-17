from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Student, Teacher, Class

class ClassInLine(admin.TabularInline):
    model = Class

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ClassInLine]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']