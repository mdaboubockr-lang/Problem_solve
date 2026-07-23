from django.contrib import admin
from django.urls import path,include
from todo_app.views import task_list_view, task_create_view, task_update_view, task_deleate_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=task_list_view.as_view(), name='list_view'),
    path('create_view/', view=task_create_view.as_view(), name='create'),
    path('update_view/<int:pk>/', view=task_update_view.as_view(), name='update'),
    path('delete_view/<int:pk>/', view=task_deleate_view.as_view(), name='delete'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('login/', view=LoginView.as_view(), name='login'),
    path('logout/', view=LogoutView.as_view(), name='logout')
]
