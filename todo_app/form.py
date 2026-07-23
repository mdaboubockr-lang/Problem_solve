from django import forms
from todo_app.models import Task

class task_create_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'task_dadline':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }