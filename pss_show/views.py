from django.http import HttpResponse
from django.shortcuts import render
import re
from redis import Redis
from pang_cmfz.settings import PERMISSION_LIST
from rbac.models import UserInfo
from rbac.service.init_permission import init_permission
redis = Redis(host='localhost', port=6379)  # 连接redis数据库
from django.views.decorators.csrf import csrf_exempt
from pang_cmfz import settings
from utils.random_code import Getcode
from utils.send_mess import YunPian


# 渲染首页的函数
def index(request):
    # 取出session中的权限列表返回前端
    per_list = request.session.get(PERMISSION_LIST)
    # 取出session中的name返回前端
    name = request.session.get("username")
    # print("index", per_list)
    print(name)
    return render(request, "index.html", {"per_list": per_list, "name": name})


# 渲染登录页面的函数
def login(request):
    return render(request, "login.html")


# 获取验证码判断的函数
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


# 登录逻辑判断的函数
@csrf_exempt
def loginlogic(request):
    # 获取用户输入的手机号、验证码、用户名
    mobile = request.POST.get('mobile')
    code = request.POST.get('code')
    name = request.POST.get('username')
    # 获取缓存中的手机号2（二进制的格式）
    res = redis.get(mobile+"02")
    print(res)
    print(code)
    # 有值判断是否相等
    if res:
        # 转换格式判断
        if res.decode('ascii') == code:
            user = UserInfo.objects.filter(name=name).first()
            if not user:
                return HttpResponse("用户名错误")
            # 完成权限相关的操作
            init_permission(user, request)
            # 用户名的欢迎
            # 将用户名存入session
            request.session["username"] = name
            return HttpResponse('ok')
        return HttpResponse('验证码输入错误')
    return HttpResponse('验证码过期')


# 退出登录
def logOut(request):
    # 清楚session中的缓存包括用户名和权限列表
    request.session.clear()
    return HttpResponse("ok")
