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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': '演员',
                'verbose_name_plural': '演员',
            },
        ),
        migrations.CreateModel(
            name='COUNTRY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': '国家',
                'verbose_name_plural': '国家',
            },
        ),
        migrations.CreateModel(
            name='DIRECTOR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': '导演',
                'verbose_name_plural': '导演',
            },
        ),
        migrations.CreateModel(
            name='FILM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='电影名称', null=True)),
                ('language', models.CharField(max_length=200, verbose_name='语言', null=True)),
                ('IMDb_link', models.CharField(max_length=200, verbose_name='IMDB链接', null=True)),
                ('intro', models.TextField(verbose_name='剧情介绍', null=True)),
                ('by_name', models.CharField(max_length=500, verbose_name='链接详情', null=True)),
                ('by_link', models.CharField(max_length=500, verbose_name='下载链接1', null=True)),
                ('pic_link', models.CharField(max_length=500, verbose_name='图片链接', null=True)),
                ('actor', models.ManyToManyField(to='film.ACTOR', related_name='actor_films', verbose_name='演员')),
                ('country', models.ForeignKey(to='film.COUNTRY', verbose_name='国家', null=True)),
                ('director', models.ManyToManyField(to='film.DIRECTOR', related_name='director_films', verbose_name='导演')),
            ],
            options={
                'verbose_name': '电影',
                'ordering': ('name',),
                'verbose_name_plural': '电影',
            },
        ),
        migrations.CreateModel(
            name='TYPE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': '类型',
                'verbose_name_plural': '类型',
            },
        ),
        migrations.CreateModel(
            name='YEAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': '年份',
                'verbose_name_plural': '年份',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='publish_year',
            field=models.ForeignKey(to='film.YEAR', verbose_name='上映年份', null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='types',
            field=models.ManyToManyField(to='film.TYPE', related_name='films', verbose_name='类型'),
        ),
    ]
