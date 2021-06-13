from django.shortcuts import render
from BaseApiView.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from istic import settings
from utils.wechat import wechatCrawler
from utils.wechatByApi import wechatCrawlerByApi
from utils.nextbtn import next_crawler
from utils.morebtn import more_crawler
import pymongo

num = 0
cnt = 0


# Create your views here.
class wechatCrawler(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["code"] = 20000
        res['data'] = wechatCrawler(request.GET['wechatName'])  # 这里可换用wechatCrawlerByApi
        return Response(res, status=status.HTTP_200_OK)


class newsCrawler(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["code"] = 20000
        mongo_client = "mongodb://localhost:27017"
        myclient = pymongo.MongoClient(mongo_client)
        dblist = myclient.list_database_names()
        if "cloud_academic" not in dblist:
            raise Exception('cloud_academic数据库不存在')
        mydb = myclient["cloud_academic"]
        collist = mydb.list_collection_names()
        content = None
        # print(collist)
        for str in collist:
            if (str == 'news_xpath'):
                content = mydb[str]
            else:
                continue
            myquery = {"website_name": request.GET['website'], "column": request.GET['column']}
            x = content.find_one(myquery)
            # print(x['web_url'], x['title_xpath'], x['content_xpath'], x['content_url'],
            #       x['time_xpath'], x['writer_xpath'], x['button_xpath'],
            #       x['website_name'], x['lang'], x['column'], x['resource_type'])
            if (x['type'] == 0):
                res['data'] = next_crawler(x['web_url'], x['title_xpath'], x['content_xpath'], x['content_url'],
                                           x['time_xpath'], x['writer_xpath'], x['button_xpath'],
                                           x['website_name'], x['lang'], x['column'], x['resource_type'])
                print(res['data'])
            else:
                res['data'] = more_crawler(x['web_url'], x['title_xpath'], x['content_xpath'], x['content_url'],
                                           x['time_xpath'], x['writer_xpath'], x['button_xpath'],
                                           x['website_name'], x['lang'], x['column'], x['resource_type'])

        myclient.close()
        return Response(res, status=status.HTTP_200_OK)


class newsCrawlerAll(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["code"] = 20000
        mongo_client = "mongodb://localhost:27017"
        myclient = pymongo.MongoClient(mongo_client)
        dblist = myclient.list_database_names()
        if "cloud_academic" not in dblist:
            raise Exception('cloud_academic数据库不存在')
        mydb = myclient["cloud_academic"]
        collist = mydb.list_collection_names()
        content = None
        content = mydb['news_xpath']
        retData = {}
        contents = content.find()
        for x in contents:
            data = {}
            if x['type'] == 0:
                data = next_crawler(x['web_url'], x['title_xpath'], x['content_xpath'], x['content_url'],
                                    x['time_xpath'], x['writer_xpath'], x['button_xpath'],
                                    x['website_name'], x['lang'], x['column'], x['resource_type'])
            else:
                data = more_crawler(x['web_url'], x['title_xpath'], x['content_xpath'], x['content_url'],
                                    x['time_xpath'], x['writer_xpath'], x['button_xpath'],
                                    x['website_name'], x['lang'], x['column'], x['resource_type'])
            resource_type = x['resource_type']
            if resource_type in retData.keys():
                retData[resource_type]['num'] += 1
                if data != None:
                    retData[resource_type]['right'] += 1
            else:
                retData[resource_type] = {'num': 1, 'right': 0}
                if data != None:
                    retData[resource_type]['right'] += 1
            # break #debug
        res['data'] = retData
        myclient.close()
        return Response(res, status=status.HTTP_200_OK)


class getProcess(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        res = {}
        res["code"] = 20000
        global num
        global cnt
        res['data'] = {'num': num, 'cnt': cnt}
        return Response(res, status=status.HTTP_200_OK)
