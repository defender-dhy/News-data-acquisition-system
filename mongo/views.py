from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from mongo.utils import *
from istic import settings
from django.views.decorators.csrf import csrf_exempt
import time
import os
from django.http import HttpResponse
from mongo.crawlStrategy import *
from mongo.xpathManage import *
from mongo.crawlLog import *
import csv
import pymongo
import codecs


# Create your views here.
class getOrganizationName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getWebSiteNameList(request.GET['database'])
        res["code"] = 20000
        return Response(res)


class getCollegeName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getColumnList(request.GET['database'], request.GET['websiteName'])
        res["code"] = 20000
        return Response(res)


class getXpathValueNameList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getXpathValueList(request.GET['valuename'])
        # print(res['data'])
        res["code"] = 20000
        return Response(res)


class getAllXpathValueNameList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["data"] = getAllXpathValueList()
        # print(res['data'])
        res["code"] = 20000
        return Response(res)


class addStrategy(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        res = {}
        ret = addNewStrategy(request.GET['strategy'])
        if ret == 1:
            res['code'] = 20000
        else:
            res['code'] = 20010
        return Response(res)


class xpathManage(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        try:
            res['data'] = getXpathManage()
            res['code'] = 20000
        except Exception as e:
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
            print(e)
        return Response(res)

    def post(self, request):
        res = {}
        ret = postXpathManage(request.GET['cont'])
        if ret == 1:
            res['code'] = 20000
        else:
            res['code'] = 20010
        return Response(res)


class getXpathByColumn(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        query = {'column': request.GET['column']}
        res['data'] = getXpathList(query)
        res['code'] = 20000
        return Response(res)


class getXpathByName(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        query = {'website_name': request.GET['website_name']}
        if request.GET['website_name'] == '':
            res['data'] = getXpathList(None)
        else:
            res['data'] = getXpathList(query)
        res['code'] = 20000
        return Response(res)


class getXpathByQuery(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        query = json.loads(request.GET['query'])
        filter = {}
        cnt = 0
        for k in query.keys():
            if query[k] != '':
                filter[k] = query[k]
                cnt += 1
        if cnt == 0:
            res['data'] = getXpathList(None)
        else:
            res['data'] = getXpathList(filter)
        res['code'] = 20000
        return Response(res)


class manageSpecXpath(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res['data'] = getXpathList(request.GET['query'])
        res['code'] = 20000
        return Response(res)

    def post(self, request):
        res = {}
        ret = modifyXpath(request.GET['filter'], request.GET['query'])
        if ret == 1:
            res['code'] = 20000
        else:
            res['code'] = 20010
        return Response(res)


class uploadXpathByFile(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        res = {}
        file = request.FILES.get('file')
        ret = addXpathByFile(file)
        if ret == 1:
            res['code'] = 20000
        else:
            res['code'] = 20010
        return Response(res)


class modifyOneSpecXpath(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        res = {}
        ret = modifyOneXpath(request.GET['cont'])
        if ret == 1:
            res['code'] = 20000
        else:
            res['code'] = 20010
        return Response(res)


class crawlerLog(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res['data'] = getAllCrawlerLog(request.GET['filter'])
        res['code'] = 20000
        return Response(res)


class crawlerSpecLog(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res['data'] = getAllSpecCrawlerLog(request.GET['filter'])
        res['code'] = 20000
        return Response(res)


class getCrawlerStrategyLs(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        key = request.GET['keyName']
        data = None
        if key == 'all':
            data = getAllStrategyLs()
        elif key == 'name':
            data = getStrategyNameList()
        elif key == 'beginDate':
            data = getStrategyBeginDateList()
        res['data'] = data
        res['code'] = 20000
        return Response(res)


class modifyLog(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        res = {}
        log = request.GET['log']
        ret = modifyLogDetail(log)
        if ret == 1:
            res['code'] = 20000
        else:
            res['code'] = 30000
        return Response(res)
