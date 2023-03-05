import django.db.models as md
from simple_history.models import HistoricalRecords

from taskmanager.models.User import User


class TaskStatus(md.TextChoices):
    NEW = "new"
    IN_PROGRESS = "in progress"
    DONE = "done"


class Task(md.Model):
    name = md.CharField(max_length=20, default="unnamed")
    description = md.CharField(max_length=2000, default="")
    status = md.CharField(max_length=12, choices=TaskStatus.choices, default=TaskStatus.NEW)
    user = md.ForeignKey(User, on_delete=md.SET_NULL, null=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['id']
