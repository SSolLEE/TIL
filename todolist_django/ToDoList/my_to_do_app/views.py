from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
'''
def index(request):
    return HttpResponse("나의 To Do List")
'''

def index(request):
    # 로직 처리 구현
    todos = Todo.objects.all() # DB에 저장된 내용 모두 가져오기
    print("From DB:", todos)
    content = {'todos' : todos}
    return render(request, "my_to_do_app/index.html", content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    print("todoContent: " + user_input_str)
    
    # DB에 저장하는 코드
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    
    #return HttpResponse("create ToDo를 하자 ==>" + user_input_str)
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    delete_todo_id = request.GET['todoNum']
    print('삭제한 todo의 id', delete_todo_id)
    todo = Todo.objects.get(id = delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))