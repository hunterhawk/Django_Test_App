# coding:utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from antiy_Encyclopedia import models
from django.core import serializers
from io import StringIO,BytesIO
import xlwt
import json
import codecs
import sys
import io
import datetime
from .models import Process_Test


# Create your views here.


def output(request):

    #response = HttpResponse(content_type='application/vnd.ms-excel')
    #response['Content-Disposition'] = 'attachment;filename=Process_Infomation.xls'



    '''
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet(u'Process_Information')
    # 1st line
    sheet.write(0, 0, 'path')
    sheet.write(0, 1, 'company')
    sheet.write(0, 2, 'product')
    sheet.write(0, 3, 'description')
    sheet.write(0, 4, 'create_time')
    sheet.write(0, 5, 'author')

    test_list_path = models.Process_Test.objects.all().values('path')
    gg = 1
    for i in test_list_path:
        for value in i.items():
            #print(value[1])
            sheet.write(gg, 0, value[1])
        gg += 1

    test_list_company = models.Process_Test.objects.all().values('company')
    gg = 1
    for i in test_list_company:
        for value in i.items():
            #print(value[1])
            sheet.write(gg, 1, value[1])
        gg += 1

    test_list_product = models.Process_Test.objects.all().values('product')
    gg = 1
    for i in test_list_product:
        for value in i.items():
            #print(value[1])
            sheet.write(gg, 2, value[1])
        gg += 1

    test_list_description = models.Process_Test.objects.all().values('description')
    gg = 1
    for i in test_list_description:
        for value in i.items():
            #print(value[1])
            sheet.write(gg, 3, value[1])
        gg += 1

    test_list_create_time = models.Process_Test.objects.all().values('create_time')
    gg = 1
    for i in test_list_create_time:
        for value in i.items():
            #print(value[1])
            sheet.write(gg, 4, value[1])
        gg += 1

    test_list_author = models.Process_Test.objects.all().values('author')
    gg = 1
    for i in test_list_author:
        for value in i.items():
            #print(value[1])
            sheet.write(gg, 5, value[1])
        gg += 1

    '''
    data1 = serializers.serialize("json", models.Process_Test.objects.all())
    #datas = models.Process_Test.objects.all()
    fl = codecs.open('H:\\Django_workspace\\test2\\templates\\download.json', 'w', encoding='utf-8')
    fl.write(json.dumps(data1, ensure_ascii=False, indent=2))
    fl.close()

    '''
    output = BytesIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response
    '''
    return render(request, 'download.json')
def down(request):
    return render(request,'download.html')

def antiyindex(request):
    all_result = Process_Test.objects.all()
    data = []
    for ele in all_result:
        _obj = {}
        _obj['path'] = ele.path
        _obj['company'] = ele.company
        _obj['product'] = ele.product
        _obj['description'] = ele.description
        _obj['create_time'] = ele.create_time.strftime("%Y-%m-%d %H:%M:%S")
        data.append(_obj)
    return HttpResponse(json.dumps(data))