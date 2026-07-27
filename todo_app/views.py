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

    def get_queryset(self):
        user = self.request.user
        search_param = self.request.GET.get("search-param", "").strip()

        queryset = Task.objects.filter(user=user)

        if search_param:
            queryset = queryset.filter(
                Q(task_sumary__icontains=search_param) |
                Q(task_deatil__icontains=search_param) |
                Q(task_status__icontains=search_param)
            )

            if search_param.isdigit():
                queryset = queryset | Task.objects.filter(
                    user=user,
                    id=int(search_param)
                )

        return queryset

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

