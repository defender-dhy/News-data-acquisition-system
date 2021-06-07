from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from mongo.utils import getColumnList,getWebSiteNameList
from istic import settings
from django.views.decorators.csrf import csrf_exempt
import time
import os
from django.http import HttpResponse
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
