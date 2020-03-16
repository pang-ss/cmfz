import json
import hashlib
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from pss_show.models import TPicture, TAlbum, TArticle, TChapter, TUser


def main(request):
    user_id = request.GET.get('uid')
    type = request.GET.get('type')
    # 存在用户id并且请求首页数据
    if user_id and type == "all":
        # 轮播图信息，最新的六张专辑信息，最新的两篇文章的信息
        pic = TPicture.objects.filter(status=1)
        album = TAlbum.objects.order_by("upload_time")[:6]
        art = TArticle.objects.order_by("upload_time")[:2]
        # json格式
        data = {
            "header": list(pic),
            "album": list(album),
            "article": list(art)
        }
        json_str = json.dumps(data, default=mydefault)
        return HttpResponse(json_str)
    # 存在用户请求专辑页面
    elif user_id and type == "wen":
        # 查询所有专辑（数据库数量较少未判断状态直接全取）
        album = TAlbum.objects.all()
        data = {
            "album": list(album)
        }
        json_str = json.dumps(data, default=mydefault)
        return HttpResponse(json_str)

    elif user_id and type == "si":
        sub_type = request.GET.get('sub_type')
        if sub_type == "ssyj":
            art = TArticle.objects.filter(type="1")
            data = {
                "article": list(art)
            }
            json_str = json.dumps(data, default=mydefault)
            return HttpResponse(json_str)
        elif sub_type =="xmfy":
            art = TArticle.objects.filter(type="2")
            print(art)
            data = {
                "article": list(art)
            }
            json_str = json.dumps(data, default=mydefault)
            return HttpResponse(json_str)
        else:
            return HttpResponse("参数可能拼写错误")
    else:
        return HttpResponse("参数拼写错误")


def mydefault(e):
    if isinstance(e, TPicture):
        return {
            "thumbnail": str(e.picture), "desc": e.description, "id": e.id
        }
    elif isinstance(e, TAlbum):
        return {
            "thumbnail": str(e.picture), "title": e.title, "author": e.author, "set_count": e.number,
            "create_date": e.upload_time.strftime("%Y-%m-%d")
        }
    elif isinstance(e, TArticle):
        return {
            "title": e.title, "content": str(e.content), "create_date": str(e.upload_time)
        }


def detail(request):
    user_id = request.GET.get("uid")
    id = request.GET.get('id')
    print(user_id,id)
    if user_id:
        album = TAlbum.objects.filter(id=id)
        chapter = TChapter.objects.filter(album_id=id)
        data = {
            "introduction": list(album),
            "list": list(chapter),
        }
        json_str = json.dumps(data, default=mydefault2)
        return HttpResponse(json_str)
    return HttpResponse("参数有误")


def mydefault2(e):
    if isinstance(e, TAlbum):
        return {
            "thumbnail": str(e.picture), "title": e.title, "level": e.level, "author": e.author, "teller": e.teller,
            "set_count": e.number,
            "content": e.content, "create_date": e.upload_time.strftime("%Y-%m-%d")
        }
    elif isinstance(e, TChapter):
        return {
            "title": e.title, "url": str(e.url), "size": e.size, "duration": e.duration
        }


@csrf_exempt
def regist(request):
    phone = request.POST.get("phone")
    password = request.POST.get('password')
    h = hashlib.sha256()
    h.update(password.encode())
    password1 = h.hexdigest()
    res = TUser.objects.filter(phone=phone)
    if res:
        data = {
            "error": "-200",
            "error_msg": "该手机号已经存在"
        }
        return JsonResponse(data)
    res = TUser.objects.create(phone=phone,password=password1)
    if res:
        user = TUser.objects.filter(phone=phone)
        json_str = json.dumps(list(user), default=mydefault3)
        return HttpResponse(json_str)
    return HttpResponse("保存失败")


def mydefault3(e):
    if isinstance(e,TUser):
        return {
            "password":e.password,"uid":e.id,"phone":e.phone
        }


@csrf_exempt
def modify(request):
    user_id = request.POST.get("uid")
    gender = request.POST.get("gender")
    photo = request.POST.get("photo")
    description = request.POST.get("description")
    nickname = request.POST.get("nickname")
    province = request.POST.get("province")
    city = request.POST.get("city")
    password = request.POST.get("password")
    user = TUser.objects.filter(id=user_id).first()
    if user:
        if gender:
            user.sex = gender
        if photo:
            user.image = photo
        if city:
            user.address_item = city
        if description:
            user.signature = description
        if nickname:
            user.username = nickname
        if province:
            user.address = province
        if password:
            h = hashlib.sha256()
            h.update(password.encode())
            password1 = h.hexdigest()
            user.password = password1
        user.save()
        user = TUser.objects.filter(id=user_id)
        json_str = json.dumps(list(user), default=mydefault4)
        return HttpResponse(json_str)
    data = {
        "error":"-200",
        "error_msg":"参数错误"
    }
    return JsonResponse(data)


def mydefault4(e):
    if isinstance(e,TUser):
        return {
            "password":e.password,
            "nickname":e.username,
            "uid":e.id,
            "gender":e.sex,
            "photo":str(e.image),
            "province":e.address,
            "city":e.address_item,
            "description":e.signature,
            "phone":e.phone
        }


