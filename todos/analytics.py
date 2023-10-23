from datetime import datetime, timedelta
from django.utils import timezone

from todos.models import TODO


class Analytic:
    def __init__(self, start_date: datetime = None, end_date: datetime = None):
        self.start_date = (
            start_date if start_date else timezone.now() - timedelta(weeks=100)
        )
        self.end_date = end_date if end_date else timezone.now()

    def get_todos(self):
        return TODO.objects.filter(
            created_at__gte=self.start_date, due_date__lte=self.end_date
        )

    def completed_tasks(self):
        return TODO.objects.filter(completed=True)

    def active_tasks(self):
        qs = TODO.objects.filter(completed=False)
        for item in qs:
            if item.status.lower() != "active":
                qs.exclude(id=item.id)
        return qs

    def inactive_tasks(self):
        return TODO.objects.exclude(id__in=self.active_tasks().values("id"))
