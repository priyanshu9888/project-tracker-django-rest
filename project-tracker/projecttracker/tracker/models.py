from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TASK_TYPES = [
        ('bug', 'Bug'),
        ('feature', 'Feature'),
        ('task', 'Task'),
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        # Add more status choices as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    task_type = models.CharField(max_length=10, choices=TASK_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    start_date = models.DateField()
    due_date = models.DateField()
    percent_done = models.IntegerField()
    description = models.TextField()
    task_number = models.CharField(max_length=20, unique=True, editable=False)

    def __str__(self):
        return f"{self.task_number} - {self.task_name}"

    def save(self, *args, **kwargs):
        # Auto-generate task number if not provided
        if not self.task_number:
            last_task = Task.objects.order_by('-id').first()
            last_task_number = last_task.task_number.split('#')[-1] if last_task else 0
            self.task_number = f"#{int(last_task_number) + 1}"

        super().save(*args, **kwargs)
