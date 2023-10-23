from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from todos.models import Tag, TODO
from todos.forms import TODOForm
from todos.analytics import Analytic


class TODOView(View):
    form_class = TODOForm
    template_name = "todos/todos_list.html"

    def get(self, request, *args, **kwargs):
        todos = TODO.objects.all()
        tags = Tag.objects.all()
        analytic = Analytic()
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "todos": todos,
                "tags": tags,
                "analytic": analytic,
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/success/")

        return render(request, self.template_name, {"form": form})
