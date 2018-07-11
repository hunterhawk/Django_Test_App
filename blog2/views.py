from django.shortcuts import render
from django.http import HttpResponse
from blog2 import models
from io import StringIO,BytesIO
import xlwt

# Create your views here.

user_list = [
    {"user":"jack", "pwd":"abc"},
    {"user":"tom", "pwd":"ABC"},
]

def index(request):
    #return HttpResponse("Hello World ! ")
    #return render(request, "index.html")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

        #print(username, password)
        temp = {"user":username, "pwd":password}
        user_list = [
            {"user": "jack", "pwd": "abc"},
            {"user": "tom", "pwd": "ABC"},
        ]
        user_list.append(temp)
    #return render(request, "index.html")
    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html",{"data":user_list})

def output(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=user.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet(u'人员表单')
    # 1st line
    sheet.write(0, 0, '用户名')
    sheet.write(0, 1, '密码')

    test_list_user = models.UserInfo.objects.all().values('user')
    kk = 1
    for i in test_list_user:
        for value in i.items():
            print(value[1])
            sheet.write(kk, 0, value[1])
        kk += 1

    test_list_pwd = models.UserInfo.objects.all().values('pwd')
    gg = 1
    for i in test_list_pwd:
        for value in i.items():
            print(value[1])
            sheet.write(gg, 1, value[1])
        gg += 1


    output = BytesIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response
def down(request):
    return render(request,'download.html')


