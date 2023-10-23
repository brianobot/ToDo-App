from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title


class TODO(models.Model):
    LEVELS = (
        ("high_priority", "High Priority"),
        ("mid_priority", "Mid Priority"),
        ("low_priority", "Low Priority"),
    )
    level = models.CharField(
        max_length=20, choices=LEVELS, default=LEVELS[1][0], blank=True
    )
    title = models.CharField(max_length=255, help_text="Title of the TODO task")
    due_date = models.DateTimeField(
        blank=True, null=True, help_text="DateTime to Complete Task before"
    )
    description = models.CharField(max_length=1000, blank=True, null=True)
    tags = models.ManyToManyField("todos.Tag", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    @property
    def status(self) -> str:
        now = timezone.now()
        if self.completed:
            return "Completed"
        else:
            if self.due_date:
                return "Active" if now <= self.due_date else "Expired"
            else:
                return "Inconclusive"

    def __str__(self) -> str:
        return f"TODO: {self.title}"
