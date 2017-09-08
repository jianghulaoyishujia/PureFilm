# coding=utf8

from django.db import models


# Create your models here.


class FILM(models.Model):
    '''
    电影
    '''
    name = models.CharField('电影名称', max_length=200, null=True)
    language = models.CharField('语言', max_length=200, null=True)
    IMDb_link = models.CharField('IMDB链接', max_length=200, null=True)
    intro = models.TextField('剧情介绍', null=True)
    by_name = models.CharField('链接详情', max_length=500, null=True)
    by_link = models.CharField('下载链接1', max_length=500, null=True)
    pic_link = models.CharField('图片链接', max_length=500, null=True)
    country = models.ForeignKey('COUNTRY', verbose_name='国家', null=True)
    publish_year = models.ForeignKey('YEAR', null=True, verbose_name='上映年份')
    director = models.ManyToManyField('DIRECTOR', related_name='director_films', verbose_name='导演')
    actor = models.ManyToManyField('ACTOR', related_name='actor_films', verbose_name='演员')
    types = models.ManyToManyField('TYPE', related_name='films', verbose_name='类型')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = '电影'
        ordering = ('name',)


class DIRECTOR(models.Model):
    '''导演'''
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '导演'
        verbose_name_plural = '导演'


class ACTOR(models.Model):
    '''演员'''
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '演员'
        verbose_name_plural = '演员'


class COUNTRY(models.Model):
    '''
    国家
    '''
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '国家'
        verbose_name_plural = '国家'


class TYPE(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = '类型'


class YEAR(models.Model):
    '''
    上映年份
    '''
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '年份'
        verbose_name_plural = '年份'
