from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=45)
    mascot = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.TextField()
    college = models.ForeignKey(College, related_name="students", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
            return f"<Student object: {self.first_name} ({self.last_name})>"