# Generated by Django 2.0.6 on 2020-03-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAdmin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 't_admin',
            },
        ),
        migrations.CreateModel(
            name='TAlbum',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('picture', models.ImageField(upload_to='img')),
                ('level', models.CharField(blank=True, max_length=20, null=True)),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('teller', models.CharField(blank=True, max_length=20, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('content', models.CharField(blank=True, max_length=5000, null=True)),
                ('datetime', models.DateField(blank=True, null=True)),
                ('space', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_album',
            },
        ),
        migrations.CreateModel(
            name='TArticle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('picture', models.ImageField(upload_to='img')),
                ('date', models.DateField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=5000, null=True)),
                ('image', models.CharField(blank=True, max_length=50, null=True)),
                ('guru_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_article',
            },
        ),
        migrations.CreateModel(
            name='TChapter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('audio', models.CharField(blank=True, max_length=100, null=True)),
                ('download', models.CharField(blank=True, max_length=50, null=True)),
                ('album_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_chapter',
            },
        ),
        migrations.CreateModel(
            name='TGuru',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('picture', models.ImageField(upload_to='img')),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 't_guru',
            },
        ),
        migrations.CreateModel(
            name='THomeworkCate',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('level', models.CharField(blank=True, max_length=20, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_homework_cate',
            },
        ),
        migrations.CreateModel(
            name='TPicture',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('picture', models.ImageField(upload_to='img')),
                ('description', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 't_picture',
            },
        ),
        migrations.CreateModel(
            name='TTimer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('count', models.CharField(blank=True, max_length=20, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('category_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_timer',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('signature', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('space', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
    ]
