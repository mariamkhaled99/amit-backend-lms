from django.db import models

from users.models import Instructor, Student
from course.models import course

# Create your models here.
class offer(models.Model):
    course_id = models.ForeignKey(course, on_delete=models.CASCADE, related_name='course_offer')
    description = models.TextField()
    enrolled_students = models.ManyToManyField(Student, related_name='enrolled_students')
    max_capacity = models.PositiveIntegerField()
    current_enrollment = models.PositiveIntegerField(default=0)
    waiting_list_status = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.course_id.course_name} {self.start_date} / {self.end_date}"
