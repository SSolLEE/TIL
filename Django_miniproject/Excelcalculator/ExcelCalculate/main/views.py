# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "main/index.html")

def signup(request):
    return render(request, "main/signup.html")

def join(request):
    print("테스트", request)
    name = request.POST.get('signupName')
    email = request.POST.get('signupEmail')
    pw = request.POST.get('signupPW')
    print("테스트2", request)
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save()
    print("사용자 정보 저장 완료됨!")
    
    return redirect("main_verifyCode")

def signin(request):
    return render(request, "main/signin.html")

def verifyCode(request):
    return render(request, "main/verifyCode.html")

def verify(request):  # 인증이 완료되면 메인 화면으로 보내줘
    return redirect('main_index')

def result(request):
    return render(request, "main/result.html")