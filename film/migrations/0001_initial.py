# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACTOR',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': '演员',
                'verbose_name': '演员',
            },
        ),
        migrations.CreateModel(
            name='COUNTRY',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': '国家',
                'verbose_name': '国家',
            },
        ),
        migrations.CreateModel(
            name='DIRECTOR',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': '导演',
                'verbose_name': '导演',
            },
        ),
        migrations.CreateModel(
            name='FILM',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='电影名称', null=True, max_length=200, unique=True)),
                ('language', models.CharField(null=True, max_length=200, verbose_name='语言')),
                ('IMDb_link', models.CharField(null=True, max_length=200, verbose_name='IMDB链接')),
                ('intro', models.TextField(null=True, verbose_name='剧情介绍')),
                ('by_name', models.CharField(null=True, max_length=5000, verbose_name='链接详情')),
                ('by_link', models.CharField(null=True, max_length=5000, verbose_name='下载链接1')),
                ('pic_link', models.CharField(null=True, max_length=500, verbose_name='图片链接')),
                ('actor', models.ManyToManyField(related_name='actor_films', to='film.ACTOR', verbose_name='演员')),
                ('country', models.ForeignKey(verbose_name='国家', null=True, to='film.COUNTRY')),
                ('director', models.ManyToManyField(related_name='director_films', to='film.DIRECTOR', verbose_name='导演')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': '电影',
                'verbose_name': '电影',
            },
        ),
        migrations.CreateModel(
            name='TYPE',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': '类型',
                'verbose_name': '类型',
            },
        ),
        migrations.CreateModel(
            name='YEAR',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': '年份',
                'verbose_name': '年份',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='publish_year',
            field=models.ForeignKey(verbose_name='上映年份', null=True, to='film.YEAR'),
        ),
        migrations.AddField(
            model_name='film',
            name='types',
            field=models.ManyToManyField(related_name='films', to='film.TYPE', verbose_name='类型'),
        ),
    ]
