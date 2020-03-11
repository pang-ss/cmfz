
from django.db import models


class TAdmin(models.Model):
    id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 't_admin'


class TAlbum(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to="image")
    level = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    teller = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    release_time = models.DateField(blank=True, null=True)
    upload_time = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 't_album'


class TArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    release_time = models.CharField(max_length=20, blank=True, null=True)
    upload_time = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    guru_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_article'


class TChapter(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    url = models.FileField(upload_to="audio")
    duration = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    album_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_chapter'


class TGuru(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to="img")
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 't_guru'


class THomeworkCate(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_homework_cate'


class TPicture(models.Model):
    id = models.IntegerField(primary_key=True)
    picture = models.ImageField(upload_to="img")
    description = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    datetime = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 't_picture'


class TTimer(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    count = models.CharField(max_length=20, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_timer'


class TUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    signature = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    address_item = models.CharField(max_length=50, blank=True, null=True)
    regist_time = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 't_user'

