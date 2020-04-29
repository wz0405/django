from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import user

# Create your views here.
def home(request):
    user_id=request.session.get('user')
    if user_id:
        User=user.objects.get(pk=user_id)
        return HttpResponse(User.username)
    return HttpResponse('Home!')
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        res_data={}
        if not (username and password):
            res_data['error']='모든 값을 입력해야합니다.'
        else:
            User=user.objects.get(username=username)
            if check_password(password, User.password):
                request.session['user'] = User.id
                return redirect('/')
            else:
                res_data['error']='비밀번호가 틀렸습니다.'

        return render(request,'login.html',res_data)
def register(request):
    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        username=request.POST.get('username',None)
        email=request.POST.get('email',None)
        password=request.POST.get('password',None)
        re_password=request.POST.get('re-password',None)
        

        res_data={}
        if not (username and password and re_password and email):
            res_data['error']='모든 값을 입력해야합니다'
        elif password!=re_password:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            User=user(
                username=username,
                email=email,
                password=make_password(password)
                
            )
            User.save()
        return render(request, 'register.html',res_data)