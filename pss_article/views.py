import json
import os
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from pss_show.models import TArticle
from pss_article.models import Pic
import datetime


def getALLArticle(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    rows = []
    article = TArticle.objects.all().order_by('id')
    all_page = Paginator(article, row_num)
    page = Paginator(article, row_num).page(page_num).object_list

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }
    for i in page:
        rows.append(i)

    def myDefault(u):
        if isinstance(u, TArticle):
            # print(u.content)
            if u.status == "1":
                return {'id': u.id,
                        'content': u.content,
                        'title': u.title,
                        'status': "展示",
                        'upload_time': u.upload_time,
                        'release_time': u.release_time,
                        }
            return {'id': u.id,
                    'content': u.content,
                    'title': u.title,
                    'status': "不展示",
                    'upload_time': u.upload_time,
                    'release_time': u.release_time,
                    }

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


# 完成富文本编辑器图片上传的功能
@xframe_options_sameorigin
@csrf_exempt
def upload_img(request):
    image = request.FILES.get('imgFile')
    if image:
        img_url = request.scheme + "://" + request.get_host() + "/static/pic/" + str(image)
        print(img_url)
        result = {"error": 0, "url": img_url}
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
        Pic.objects.create(img=image, datetime=date)
    else:
        result = {"error": 0, "message": "上传出错"}

    return JsonResponse(result)


# 获取层上传过的所有图片
def get_all_img(request):
    """
    获取所有层上传过得图片
    :param request:
    :return: 所有图片以及对应的参数
    """
    # 找到图片所在的路径  方便回显
    pic_url = request.scheme + "://" + request.get_host() + "/static/"
    print(pic_url)
    # 获取所有曾上传过得图片
    pic_all = Pic.objects.all()
    rows = []
    for pic in list(pic_all):
        # 获取图片后缀名
        path, pic_suffix = os.path.splitext(pic.img.url)
        date = pic.datetime
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": pic.img.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": pic.img.name,
            "datetime": date
        })
    # 图片空间所需的所有数据
    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_url,
        "total_count": len(pic_all),
        "file_list": rows
    }
    return JsonResponse(data)


# 添加文章
def add_article(request):
    title = request.GET.get("title")
    release_time = request.GET.get("release_time")
    upload_time = request.GET.get("upload_time")
    status = request.GET.get("status")
    content = request.GET.get("content")
    print(title, status, content, release_time, upload_time)
    res = TArticle.objects.create(title=title, release_time=release_time, upload_time=upload_time, content=content,
                                  status=status)
    # 将文章的相关信息存入数据库
    if res:
        return HttpResponse("ok")
    return HttpResponse('no')


# 修改文章内容
def change_article(request):
    id = request.GET.get("id")
    # print(id)
    title = request.GET.get("title")
    release_time = request.GET.get("release_time")
    upload_time = request.GET.get("upload_time")
    status = request.GET.get("status")
    content = request.GET.get("content")
    res = TArticle.objects.get(id=id)
    if res:
        res.title = title
        res.release_time = release_time
        res.upload_time = upload_time
        res.status = status
        res.content = content
        res.save()
        return HttpResponse('ok')
    return HttpResponse('no')


@csrf_exempt
def edit_article(request):
    operation = request.POST.get('oper')
    id = request.POST.get('id')
    if operation == 'del':
        TArticle.objects.get(id=id).delete()
    return HttpResponse('ok')