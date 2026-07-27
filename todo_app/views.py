from django.shortcuts import render
from django.views.generic import ListView
from todo_app.models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from todo_app.form import task_create_form
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from todo_app.models import Task
from django.db.models import Q


class task_list_view(LoginRequiredMixin, ListView):
    model = Task
    template_name = "Task_list.html"
    context_object_name = "all_list"

    def get_context_data(self, **kwargs):

        user = self.request.user
        serach_param = self.request.GET.get('search-param', None)
        task_list = Task.objects.filter(user=user)

        task_list = task_list.filter(
            Q(task_sumary__icontains=serach_param)|
            Q(task_detail__icontains=serach_param)|
            Q(task_status__icontains=serach_param)|
            Q(id=int(serach_param)) if serach_param and serach_param.isdigit() else Q()
        )

        context = super().get_context_data(**kwargs)
        context["task_list"] = task_list
        return context

class task_create_view(CreateView):
    template_name = 'Task_create.html'
    form_class = task_create_form
    success_url = reverse_lazy('list_view')
    context_object_name = 'form'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class task_update_view(UpdateView):
    model = Task
    template_name = 'Task_update.html'
    form_class = task_create_form
    success_url = reverse_lazy('list_view')

class task_deleate_view(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('list_view')

