from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render



# ToDoの一覧表示機能
class TodoListView(generic.ListView):
    model = Todo
    paginate_by = 5
    template_name = 'todo/todo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TODO_LIST'] = Todo.objects.filter(status=1).all()

        return context


# ToDoの詳細表示機能
class TodoDetailView(generic.DetailView):
    model = Todo

# ToDoの作成機能
class TodoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

# ToDoの編集機能
class TodoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

# ToDoの削除機能
class TodoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')


def user_information(request):
    print(request.user.username)
    # test
    print(request.user.email)
    # test@yahoo.co.jp
    print(request.user.is_active)
    # True
    print(request.user.is_staff)
    # False
    print(request.user.is_superuser)
    # False

