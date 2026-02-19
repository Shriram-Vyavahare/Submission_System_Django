from django.db import models

class Assignment(models.Model):
    student_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='assignments/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
