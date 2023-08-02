from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from random import *
from sendEmail.views import *

# Create your views here.
def index(request):
    if 'user_name' in request.session.keys():
        return render(request, "main/index.html")
    else:
        return redirect("main_signin")

def signup(request):
    return render(request, "main/signup.html")

def join(request):
    print("테스트", request)
    
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save()

    print("사용자 정보 저장 완료됨!")

    # 인증 코드 1000~9000 랜덤으로 하나 생성
    code = randint(1000, 9000)
    print("인증 코드 생성---------", code)

    response = redirect("main_verifyCode") # 응답을 객체로 저장
    response.set_cookie('code', code) # 인증 코드
    response.set_cookie('user_id', user.id)

    print("응답 객체 완성 ----------", response)
    # 이메일 발송 함수 호출
    send_result = send(email, code)
    if send_result:
        print("Main > views.py > 이메일 발송 중 완료된 거 같음....")
        return response
    else:
        return HttpResponse("이메일 발송 실패!")    


def signin(request):
    return render(request, "main/signin.html")

def login(request):
    # 로그인된 user만 이용할 수 있도록 구현
    # 로그인 user 판단을 위해 세션 사용(verify함수)
    # 세션 처리 진행
    loginEmail = request.POST['loginEmail']
    loginPW = request.POST['loginPW']
    user = User.objects.get(user_email = loginEmail)
    if user.user_password ==loginPW:
        request.session['user_name'] = user.user_name # user가 회원가입 시 입력한 정보
        request.session['user_email'] = user.user_email # user가 회원가입 시 입력한 정보
        return HttpResponse("test")
    

def verifyCode(request):
    return render(request, "main/verifyCode.html")

def verify(request):  
    # user가 입력한 code값을 받아야 함
    user_code = request.POST['verifyCode']
    # 쿠키에 저장된 코드를 불러옴(join함수 확인)
    cookie_code = request.COOKIES.get('code')
    print("코드 확인: ", user_code, cookie_code)

    if user_code == cookie_code:
        user=User.objects.get(id=request.COOKIES.get('user_id'))
        user.user_validate = 1 # True 1, False 0
        user.save()

        print("DB에 user_validate 업데이트-------")

        response = redirect('main_index')

        # 저장되어 있는 쿠키를 삭제
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        # response.set_cookie('user', user)
        # 사용자 정보를 세션에 저장
        request.session['user_name'] = user.user_name   # 로그인화면 구현
        request.session['user_email'] = user.user_email # 로그인화면 구현
        
        return response

    return redirect('main_index')

def result(request):
    if 'user_name' in request.session.keys():
        return render(request, "main/result.html")
    else:
        return redirect("main_signin")
    # return render(request, "main/result.html")

def logout(request):
    del request.session['user_name']
    del request.session['user_email']

    return redirect('main_signin')