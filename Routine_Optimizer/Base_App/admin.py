from django.contrib import admin
from .models import day ,subject,section ,room , period ,faculty, schedule ,class_no

# Register your models here.
@admin.register(day)
class DaysAdmin(admin.ModelAdmin):
    list_display = ('day_name',)

@admin.register(subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('sub_name',)


@admin.register(section)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('sec_name',)

@admin.register(class_no)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('class_name',)

@admin.register(room)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_no',)


@admin.register(period)
class PeriodsAdmin(admin.ModelAdmin):
    list_display = ('period_number', 'start_time', 'end_time', 'is_break')
    list_filter = ['is_break']

@admin.register(faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'faculty_department', 'faculty_email')
    search_fields = ('faculty_name', 'faculty_email', 'faculty_department')
    filter_horizontal = ('subjects',)

@admin.register(schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'day', 'period', 'subject', 'section', 'room')
    list_filter = ('day', 'faculty__faculty_department')
    search_fields = ('faculty__faculty_name', 'subject__sub_name')
