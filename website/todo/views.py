from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def todo_page(request):
    return render(request, 'todo/todo.html')