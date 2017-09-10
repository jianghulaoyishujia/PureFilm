from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
# from utils.pager_helper import PageHelper
from film.models import TYPE, COUNTRY, DIRECTOR, YEAR, ACTOR, FILM
from django.db.models import Q
from K_Movies.映射表 import *
from django.views.decorators.csrf import csrf_exempt
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from time import sleep
import requests
import json
import os


# Create your views here.

# def index(request):
# films = models.FILM.objects.all()
# film_list = models.FILM.objects.all()
# paginator = Paginator(film_list, 25)
# page = request.GET.get('page')
# try:
#     films = paginator.page(page)
# except PageNotAnInteger:
#     films = paginator.page(1)
# except EmptyPage:
#     films = paginator.page(paginator.num_pages)
# return render(request, 'index.html', {"films": films})
# print('fuck, 确实带了参数')



def index(request):
    '''
    首页显示
    '''
    Data = request.GET
    ftype = Data.get('ftype')
    country = Data.get('country')
    year = Data.get('year')  # 如果为空返回的居然是字符串'None' 奇葩
    # print(year, type(year), year == 'None')
    # print(country, type(country))
    try:


        type_num = film_type_table.get(ftype)
        country_num = film_country_table.get(country)


        if type_num:
            films1 = FILM.objects.filter(types=type_num)
        else:
            films1 = FILM.objects.all()


        if country_num:
            films2 = films1.filter(country=country_num)
        else:
            films2 = films1.all()


        print('type'+ftype)
        print('country'+country)
        print('year' + year)
        if year == 'None' or year=='year_all':
            films = films2
        elif year:
            # print(year is 'None')
            year_list1 = ['2017', '2016', '2015', '2014', '2013', '2012', '2011']
            year_list2 = ['100', '90', '80', '70']
            if year in year_list1:
                films3 = films2.filter(publish_year__name=year)
            elif year in year_list2:
                films3 = films2.filter(publish_year__name__in=[str(1900 + int(year) + x) for x in range(10)])
            else:
                films3 = films2.filter(publish_year__name__lt=1960)  # got you
            films = films3
        else:
            films = films2

    except Exception:
        # films = FILM.objects.all().distinct()[obj.db_start:obj.db_end]
        films = FILM.objects.all()

    current_page = request.GET.get("p", 1)
    current_page = int(current_page)
    total_count = films.all().count()
    obj = PageHelper(total_count, current_page, "/", 24, ftype, country, year)
    v = (total_count // 20) - 2
    pager = obj.page_str()
    films = films.distinct()[obj.db_start:obj.db_end]
    return render(request, 'index.html', locals())


def film(request, id):
    try:
        film = get_object_or_404(FILM, id=id)
        keys = film.by_name.split(",")
        values = film.by_link.split(",")
        dic = {}
        for x, y in zip(keys, values):
            dic[x] = y
        return render(request, 'film.html', {'film': film, 'dic': dic})
    except Exception:
        return redirect('/')


@csrf_exempt
def addFilm(request):
    if not os.path.exists('fuck'):
        os.mkdir('fuck')
    if request.method == "POST":
        r = request.body
        data = json.loads(r.decode('utf-8'))
        name = data['name'][:-6]
        language = data['language']
        IMDb_link = data['IMDb_link']
        intro = data['intro']
        try:
            pic_link = data['pic_link']
            pic_name = pic_link.split('/')[-1][:-6]
            try:
                urlretrieve(pic_link, ('statics/fuck/%s' % pic_name))
                print(pic_name)
                sleep(3)
            except:
                download_pic(pic_link, ('statics/fuck/%s' % pic_name))
        except:
            pic_name = '暂无'
            pic_link = 'fuck/kwell.jpg'

        d_name, d_link = '', ''
        for x, y in zip(data['link_name'], data['download_link']):
            d_name = d_name + ',' + x
            d_link = d_link + ',' + y

        country = data['country']
        try:
            country = COUNTRY.objects.filter(name=country)[0]
        except:
            country = COUNTRY.objects.create(name=country)

        publish_year = data['name'][-5:-1]
        try:
            publish_year = YEAR.objects.filter(name=publish_year)[0]
        except:
            publish_year = YEAR.objects.create(name=publish_year)

        director = '暂无'

        # ————————————————————————————————————————新建一个电影项-------------------------------------------------------
        newfilm = FILM.objects.create(
            name=name,
            publish_year=publish_year,
            language=language,
            IMDb_link=IMDb_link,
            intro=intro,
            pic_link='fuck/%s' % pic_name,
            by_name=d_name,
            by_link=d_link,
            country=country
        )
        newfilm.save()
        # ------------------------------------------给新建的电影项添加外键和多对多关系-------------------------------------
        try:
            actors = data['actor'].split()
            for actor in actors:
                try:
                    newfilm.actor.add(ACTOR.objects.filter(name=actor)[0])
                except Exception:
                    newfilm.actor.create(name=actor)
        except:
            actor = '暂无'
            newfilm.actor.add(ACTOR.objects.filter(name=actor))

        try:
            newfilm.director.add(DIRECTOR.objects.filter(name=director)[0])
            print('找到了一个导演')
        except:
            newfilm.director.create(name=director)
            print('新建了一个导演')

        try:
            f_types = data['types'].split()
            for f_type in f_types:
                try:
                    newfilm.types.add(TYPE.objects.filter(name=f_type)[0])
                except:
                    newfilm.types.create(name=f_type)
        except:
            f_type = '暂无'
            newfilm.types.add(TYPE.objects.filter(name=f_type))

        return HttpResponse('YES')
    else:
        return HttpResponse('FUCK OFF ')


def download_pic(pic_url, name):
    urlretrieve(pic_url, '%s.jpg' % name)
    print('picutre downloaded')


def search(request):
    key_word_buttorn = request.GET.get('key')  # button用GET方法
    key_word_backspace = request.POST.get('f1')  # backspace用POST方法
    key_word = key_word_buttorn or key_word_backspace
    # print('GET数据传输正确')
    # films = FILM.objects.filter(name__contains=key_word)
    films = FILM.objects.filter(Q(name__contains=key_word) | Q(actor__name__contains=key_word)).distinct()
    print(films)
    return render(request, 'search_result.html', {"films": films})


class PageHelper:
    def __init__(self, total_count, p, base_url, per_page, ftype, country, year):
        self.total_count = total_count
        self.current_page = p
        self.base_url = base_url
        self.per_page = per_page
        self.ftype = ftype
        self.country = country
        self.year = year
        pass

    @property
    def db_start(self):
        return (self.current_page - 1) * self.per_page

    @property
    def db_end(self):
        return self.current_page * self.per_page

    def total_page(self):
        v, a = divmod(self.total_count, self.per_page)
        if a != 0:
            v += 1
        return v

    def page_str(self):
        v = self.total_page()
        pager_list = []
        if self.current_page == 1:
            pager_list.append('<a href="javascript:void(0);">上一页</a>')
        else:
            pager_list.append('<a href="%s?p=%s&ftype=%s&country=%s&year=%s">上一页</a>' %
                              (self.base_url, self.current_page - 1, self.ftype, self.country, self.year,))

        if v <= 11:
            pager_range_start = 1
            pager_range_end = v
        else:
            if self.current_page < 6:
                pager_range_start = 1
                pager_range_end = 11 + 1
            else:
                pager_range_start = self.current_page - 5
                pager_range_end = self.current_page + 6
                if pager_range_end > v:
                    pager_range_start = v - 10
                    pager_range_end = v + 1

        for i in range(pager_range_start, pager_range_end):
            if i == self.current_page:
                pager_list.append('<a class="active" href="%s?p=%s&ftype=%s&country=%s&year=%s">%s</a>' % (
                    self.base_url, i, self.ftype, self.country, self.year, i,))
            else:
                pager_list.append('<a href="%s?p=%s&ftype=%s&country=%s&year=%s">%s</a>' % (
                    self.base_url, i, self.ftype, self.country, self.year, i,))
        if self.current_page == v:
            pager_list.append('<a href="javascript:void(0);">下一页</a>')
        else:
            pager_list.append('<a href="%s?p=%s&ftype=%s&country=%s&year=%s">下一页</a>' %
                              (self.base_url, self.current_page + 1, self.ftype, self.country, self.year,))

        pager = " ".join(pager_list)
        return pager
