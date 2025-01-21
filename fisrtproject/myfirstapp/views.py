from django.shortcuts import render
from .models import test_collection
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def add_rec(request):
    records = {"rec1":1}
    test_collection.insert_one(records)
    return HttpResponse("new record is added")

def get_all_rec(request):
    recs = test_collection.find()
    return HttpResponse(recs)



def register(request):
    return render(request, "register.html")

def regadd(request):
    userid=request.POST['userid']
    account=request.POST['account']
    password=request.POST['password']
    username=request.POST['username']
    gender=request.POST['gender']
    age=request.POST['age']
    print(userid, account, password, username, gender, age)  # 在後台(終端)輸出

    user_document = {
    "userid": userid,
    "account": account,
    "password": password,
    "username": username,
    "gender": gender,
    "age": age}

    test_collection.insert_one(user_document)  # 永久化到DB
    return redirect("/userlist/1/")



def userlist(request, curpage):
    print("here is userlist.html page " + curpage)
    data_pagesize = 10  # 每頁資料數量
    data_pagestart = (int(curpage) - 1) * data_pagesize  # 起始索引

    # 獲取總資料數量
    datacount = test_collection.count_documents({})
    maxpage = datacount // data_pagesize if datacount % data_pagesize == 0 else datacount // data_pagesize + 1

    # 分頁查詢資料
    myusers = test_collection.find().skip(data_pagestart).limit(data_pagesize)

    # 整理資料
    myusers2 = []
    for user in myusers:
        myusers2.append(user)  # 直接將 MongoDB 的 document 轉為字典

    # 計算上一頁與下一頁
    myprev = 1 if int(curpage) == 1 else int(curpage) - 1
    mynext = int(curpage) + 1 if int(curpage) < maxpage else int(curpage)

    # 構建分頁資訊
    mypage = {"myprev": myprev, "mynext": mynext, "last": maxpage, "first": 1}

    return render(request, 'userlist.html', context={'myusers2': myusers2, 'mypage': mypage, 'curpage': curpage})