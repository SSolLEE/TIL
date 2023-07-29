from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def index(request):
    return HttpResponse("나의 To Do List")
'''

def index(request):
    return render(request, "my_to_do_app/index.html")

def createTodo(request):
    user_input_str = request.POST['todoContent']
    print("todoContent: " + user_input_str)
    return HttpResponse("create ToDo를 하자 ==>" + user_input_str)