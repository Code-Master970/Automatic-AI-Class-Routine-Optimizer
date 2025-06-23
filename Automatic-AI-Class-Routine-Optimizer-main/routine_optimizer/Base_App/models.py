from django.db import models
from django.core.exceptions import ValidationError

class day(models.Model):
    day_name = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.day_name

class subject(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.sub_name
    
class class_no(models.Model):
    class_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.class_name

class section(models.Model):
    sec_name = models.CharField(max_length=10, default="A", unique=True)
    def __str__(self):
        return self.sec_name

class room(models.Model):
    room_no = models.CharField(max_length=5, unique=True)
    def __str__(self):
        return self.room_no

# class period(models.Model):
#     start_time = models.TimeField()
#     end_time = models.TimeField(null=True, blank=True)
#     period_number = models.IntegerField(null=True, blank=True)
#     def __str__(self):
#         return f"Period {self.period_number}: {self.start_time} - {self.end_time}"

class period(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    period_number = models.IntegerField(null=True, blank=True)
    is_break = models.BooleanField(default=False)

    def __str__(self):
        label = "Break" if self.is_break else f"Period {self.period_number}"
        return f"{label}: {self.start_time} - {self.end_time}"

class faculty(models.Model):
    faculty_name = models.CharField(max_length=100)
    # faculty_email = models.EmailField(unique=True)
    # faculty_department = models.CharField(max_length=50)
    college_id = models.CharField(max_length=25,default='DSC-1000')
    subjects = models.ManyToManyField('subject', related_name='faculties')

    def __str__(self):
        return f"{self.faculty_name} ({self.college_id})"

from django.core.exceptions import ValidationError

class schedule(models.Model):
    faculty = models.ForeignKey('faculty', on_delete=models.CASCADE, related_name='schedules')
    day = models.ForeignKey('day', on_delete=models.CASCADE)
    period = models.ForeignKey('period', on_delete=models.CASCADE)
    subject = models.ForeignKey('subject', on_delete=models.CASCADE)
    class_no = models.ForeignKey('class_no', on_delete=models.CASCADE, null=True, blank=True)
    section = models.ForeignKey('section', on_delete=models.CASCADE)
    room = models.ForeignKey('room', on_delete=models.CASCADE)
    is_lab = models.BooleanField(default=False) #for lab
    active = models.BooleanField(default=False)

    class Meta:
        unique_together = [
            ('faculty', 'day', 'period'),
            ('room', 'day', 'period')
        ]
        ordering = ['day', 'period']

    def __str__(self):
        return f"{self.faculty.faculty_name} teaches {self.subject.sub_name} to {self.section.sec_name} on {self.day.day_name} at {self.period}"

    def clean(self):
        # ❌ Prevent assigning a subject during break
        if self.period.is_break:
            raise ValidationError("Cannot assign subject to a break period.")

        # ✅ Check if faculty is allowed to teach the subject
        if not self.faculty.subjects.filter(id=self.subject.id).exists():
            raise ValidationError(f"{self.faculty.faculty_name} is not assigned to teach {self.subject.sub_name}")

        # ❌ Check valid time range
        if self.period.end_time and self.period.start_time >= self.period.end_time:
            raise ValidationError("End time must be after start time")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

