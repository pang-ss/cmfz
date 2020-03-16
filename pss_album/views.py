import json
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mutagen.mp3 import MP3
from pss_show.models import TAlbum, TChapter


def getAllAlbum(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    rows = []
    album = TAlbum.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)
    for i in page:
        rows.append(i)
    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TAlbum):
            print(u.title)
            if u.status == "1":
                return {
                    "author": u.author,
                    "content": u.content,
                    "teller": u.teller,
                    "number": u.number,
                    "picture": str(u.picture),
                    "release_time": u.release_time.strftime('%Y-%m-%d'),
                    "id": u.id,
                    "upload_time": u.upload_time.strftime('%Y-%m-%d'),
                    "level": u.level,
                    "status": "展示",
                    "title": u.title,
                }
            return {
                "author": u.author,
                "content": u.content,
                "teller": u.teller,
                "number": u.number,
                "picture": str(u.picture),
                "release_time": u.release_time.strftime('%Y-%m-%d'),
                "id": u.id,
                "upload_time": u.upload_time.strftime('%Y-%m-%d'),
                "level": u.level,
                "status": "不展示",
                "title": u.title,
            }

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


# 添加专辑
@csrf_exempt
def add_album(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    teller = request.POST.get('teller')
    content = request.POST.get('content')
    number = request.POST.get('number')
    release_time = request.POST.get('release_time')
    upload_time = request.POST.get('upload_time')
    level = request.POST.get('level')
    status = request.POST.get('status')
    picture = request.FILES.get('picture')
    res = TAlbum.objects.create(title=title, author=author, teller=teller, content=content, number=number,
                                release_time=release_time, upload_time=upload_time, level=level, status=status,
                                picture=picture)
    if res:
        return HttpResponse('ok')
    return HttpResponse('no')


# 展示章节
def getChapter(request):
    albumId = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    rows = []
    album = TChapter.objects.all().filter(album_id=albumId).order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)
    for i in page:
        rows.append(i)
    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TChapter):
            return {
                "albumId": u.album_id,
                "create_time": u.create_time.strftime("%Y-%m-%d"),
                "duration": u.duration,
                "id": u.id,
                "size": u.size,
                "title": u.title,
                "url": str(u.url),
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


# 添加章节
@csrf_exempt
def add_chapter(request):
    album_id = request.POST.get('albumId')
    chapterTitle = request.POST.get('chapterTitle')
    create_time = request.POST.get('create_time')
    audio = request.FILES.get('audio')
    file = MP3(audio)
    duration = file.info.length  # 音频时长
    size = audio.size
    res = TChapter.objects.create(title=chapterTitle, create_time=create_time, url=audio, duration=duration, size=size,
                                  album_id=album_id)
    if res:
        return HttpResponse('ok')
    return HttpResponse('no')


# 删除专辑
@csrf_exempt
def edit_album(request):
    operation = request.POST.get('oper')
    id = request.POST.get('id')
    if operation == 'del':
        TAlbum.objects.get(id=id).delete()
    return HttpResponse('ok')


# 修改专辑
@csrf_exempt
def change_album(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    author = request.POST.get('author')
    teller = request.POST.get('teller')
    content = request.POST.get('content')
    number = request.POST.get('number')
    release_time = request.POST.get('release_time')
    upload_time = request.POST.get('upload_time')
    level = request.POST.get('level')
    status = request.POST.get('status')
    picture = request.FILES.get('picture')
    res = TAlbum.objects.get(id=id)
    if res:
        res.title = title
        res.author = author
        res.teller = teller
        res.content = content
        res.number = number
        res.release_time = release_time
        res.upload_time = upload_time
        res.level = level
        res.status = status
        res.picture = picture
        res.save()
        return HttpResponse('ok')
    return HttpResponse('no')


# 删除章节
@csrf_exempt
def edit_chapter(request):
    operation = request.POST.get('oper')
    id = request.POST.get('id')
    if operation == 'del':
        TChapter.objects.get(id=id).delete()
    return HttpResponse('ok')


# 修改章节
@csrf_exempt
def change_chapter(request):
    id = request.POST.get('id')
    title = request.POST.get('chapterTitle')
    create_time = request.POST.get('create_time')
    audio = request.FILES.get('audio')
    file = MP3(audio)
    duration = file.info.length  # 音频时长
    size = audio.size
    res = TChapter.objects.get(id=id)
    if res:
        res.title = title
        res.create_time = create_time
        res.audio = audio
        res.duration = duration
        res.size = size
        res.save()
        return HttpResponse('ok')
    return HttpResponse('no')