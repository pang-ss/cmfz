# from django.shortcuts import render, redirect
# # Create your views here.
# from rbac.models import UserInfo
# from rbac.service.init_permission import init_permission
#
#
# def login(request):
#     return render(request, "rbac_login.html")
#
#
# def check_user(request):
#     if request.method == "GET":
#         return render(request, "rbac_login.html", {'msg': "请求方法不正确"})
#     name = request.POST.get('name')
#     pwd = request.POST.get('pwd')
#     user = UserInfo.objects.filter(name=name, password=pwd).first()
#     if not user:
#         return render(request, "rbac_login.html", {"msg": "用户名或密码不正确"})
#     # 完成权限相关的操作
#     init_permission(user, request)
#     # 用户需要重定向到首页
#     return redirect('/show/index')
