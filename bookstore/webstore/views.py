from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def add_book(request):
    if request.method == 'GET':
        return render(request, 'new_book.html')
    elif request.method == "POST":
        title = request.POST.get('title', '')
        pub = request.POST.get('pub', '')
        price = request.POST.get('price', '')
        market_price = request.POST.get('market_price', '')
        abook = models.Books.objects.create(title=title, pub=pub, price=price, market_price=market_price)
        print('添加新书：', abook.title)
        return HttpResponse('<a href="/webstore">添加成功，点击返回首页</a>')


def show_book(request):
    book = models.Books.objects.all()
    return render(request, 'all_book.html', locals())


def search(request):
    title = request.GET.get("title")
    book = models.Books.objects.filter(title__contains=title)
    return render(request, "all_book.html", locals())


def mod_book(request, book_id):
    if request.method == 'GET':
        return render(request, "mod_book.html", locals())
    elif request.method == 'POST':
        try:
            abook = models.Books.objects.get(id=book_id)
            # m_title = request.POST.get('title', '')
            # m_pub = request.POST.get('pub', '')
            m_price = request.POST.get('price', '0.0')
            m_market_price = request.POST.get('market_price', '0.0')
            # abook.title = m_title
            # abook.pub = m_pub
            abook.price = m_price
            abook.market_price = m_market_price
            abook.save()
            return HttpResponse("修改成功")
        except:
            return HttpResponse("修改失败")


from django.http import HttpResponseRedirect


def del_book(request, book_id):
    abook = models.Books.objects.get(id=book_id)
    abook.delete()
    return HttpResponseRedirect('/webstore/show_book')
