from django.shortcuts import render
from django.views.generic import ListView
from todo_app.models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from todo_app.form import task_create_form
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from todo_app.models import Task



class task_list_view(LoginRequiredMixin, ListView):
    model = Task
    template_name = "Task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_list"] = Task.objects.all()
        return context


class task_create_view(CreateView):
    template_name = 'Task_create.html'
    form_class = task_create_form
    success_url = reverse_lazy('list_view')
    context_object_name = 'form'



class task_update_view(UpdateView):
    model = Task
    template_name = 'Task_update.html'
    form_class = task_create_form
    success_url = reverse_lazy('list_view')

class task_deleate_view(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('list_view')