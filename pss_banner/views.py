import json

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
from pss_show.models import TPicture


# 向数据库添加一张轮播图
@csrf_exempt
def add_banner(request):
    title = request.POST.get('title')
    status = request.POST.get('status')
    picture = request.FILES.get('pic')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(title, status, picture, date)
    res = TPicture.objects.create(description=title, status=status, picture=picture, datetime=date)
    if res:
        return HttpResponse('ok')
    return HttpResponse('no')


# 展示
def get_banner(request):
    rowNum = request.GET.get('rows')
    pageNum = request.GET.get('page')
    res = TPicture.objects.all()
    pgntor = Paginator(res, rowNum)
    #  创建当前page对象
    pg = pgntor.page(pageNum)
    re_data = {
        "page": pageNum,
        "total": pgntor.num_pages,
        "records": pgntor.count,
        "rows": list(pg)
    }
    json_str = json.dumps(re_data, default=mydefault)
    # print(json_str)
    return HttpResponse(json_str)


def mydefault(e):
    if isinstance(e, TPicture):
        # 判断轮播图的显示状态 e.status 等于1是显示
        # print(e.status)
        # print(type(e.status))
        if e.status == "1":
            return {'id': e.id, "title": e.description, "status": "显示", "pic": str(e.picture), "create_time": e.datetime}
        return {'id': e.id, "title": e.description, "status": "不显示", "pic": str(e.picture), "create_time": e.datetime}


# 修改轮播图信息
@csrf_exempt
def change_banner(request):
    operation = request.POST.get('oper')
    id = request.POST.get('id')
    if operation == "edit":
        title = request.POST.get('title')
        status = request.POST.get('status')
        res = TPicture.objects.get(id=id)
        res.description = title
        res.status = status
        res.save()
    elif operation == 'del':
        TPicture.objects.get(id=id).delete()
    return HttpResponse('ok')

