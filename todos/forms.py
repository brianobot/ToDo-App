from django import forms

from todos.models import TODO


class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = [
            "title",
            "description",
            "due_date",
            "level",
            "tags",
            "completed",
        ]
