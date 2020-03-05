import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
import re
from redis import Redis

from pss_show.models import TPicture, TUser

redis = Redis(host='localhost',port=6379)  # 连接redis数据库

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from pang_cmfz import settings
from utils.random_code import Getcode
from utils.send_mess import YunPian


def index(request):
    # # 判断是否登录
    # res = request.session.get("islogin")
    # if res:
    #     # 登录返回首页
    #     return render(request, "index.html")
    # # 未登录返回登录页面
    # return redirect('pss_show:login')
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


@csrf_exempt
def get_code(request):
    mobile = request.POST.get('mobile')
    print(mobile)
    # 查询数据库中是否有此手机号
    res = redis.get(mobile+"01")
    print(res)
    # 如果有值，60s内已经发送过验证码，返回前端提示
    if res:
        return HttpResponse('发送频繁稍后重试')
    # 否则正则判断手机号格式
    ret = re.match(r"^1[35678]\d{9}$", mobile)
    # 格式正确
    if ret:
        # 创建对象
        yunpian = YunPian(settings.APIKEY)
        # 生成六位验证码
        code = Getcode().code()
        # 发送验证码
        yunpian.send_message(mobile, code)
        mobile1 = mobile + "01"
        mobile2 = mobile + "02"
        # 存入redis60s后才可重新发送
        redis.setex(mobile1, 60, code)
        # 存入redis300s后验证码失效
        redis.setex(mobile2, 300, code)
        return HttpResponse('ok')
    else:
        return HttpResponse('手机号格式不正确')


@csrf_exempt
def loginlogic(request):
    mobile = request.POST.get('mobile')
    code = request.POST.get('code')
    username = request.POST.get('username')
    ret = re.match(r"^.{2,}$", username)
    if ret:
        res = redis.get(mobile+"02")
        print(res)
        print(code)
        # 有值判断是否相等
        if res:
            if res.decode('ascii') == code:
                # 通过存入数据库返回首页
                request.session['islogin'] = True
                res = TUser.objects.create(username=username,phone=mobile)
                if res:
                    return HttpResponse('ok')
            return HttpResponse('验证码输入错误')
        return HttpResponse('验证码过期')
    return HttpResponse('用户名不符合')



