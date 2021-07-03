from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from mongo.utils import getColumnList, getWebSiteNameList, getXpathValueList
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
        res['data'] = getXpathManage()
        res['code'] = 20000
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
        res['data'] = getXpathList(query)
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
