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
from utils.nextButton import nextBtn_crawler
from utils.moreButton import moreBtn_crawler
from utils.nextButton import processManage
import pymongo
from mongo.crawlLog import *

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
            # print(x['type'])
            if x['type'] == '0':
                print(x['type'])
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
                # print("*******************")
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


class newsCrawlerOne(APIView):
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
        content = mydb['news_xpath']
        manage = mydb['news_xpath_manage']
        myquery = {"website_name": request.GET['website'], "column": request.GET['column']}
        x = content.find_one(myquery)
        xpathInfo = processManage(manage)
        if x['type'] == '0':
            res['data'] = nextBtn_crawler(x, xpathInfo)
        else:
            res['data'] = moreBtn_crawler(x, xpathInfo)
        myclient.close()
        return Response(res, status=status.HTTP_200_OK)


# class newsCrawlerMany(APIView):
#     '''
#     获取数据源list, 更新数据源爬取进度
#     '''
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request):
#         global crawler_many_process
#         crawler_many_process = 0
#         res = {}
#         res["code"] = 20000
#         mongo_client = "mongodb://localhost:27017"
#         myclient = pymongo.MongoClient(mongo_client)
#         dblist = myclient.list_database_names()
#         if "cloud_academic" not in dblist:
#             raise Exception('cloud_academic数据库不存在')
#         mydb = myclient["cloud_academic"]
#         content = mydb['news_xpath']
#         manage = mydb['news_xpath_manage']
#         urlList = request.GET['url_list']
#         urlList = urlList.split(',')
#         resList = []
#         xpathInfo = processManage(manage)
#         for url in urlList:
#             myquery = {'web_url': url}
#             x = content.find_one(myquery)
#             if len(x) == 0:
#                 continue
#             if x['type'] == '0':
#                 resList.append(nextBtn_crawler(x, xpathInfo))
#             else:
#                 resList.append(moreBtn_crawler(x, xpathInfo))
#             crawler_many_process = crawler_many_process + 100 / len(queryList)
#         res['data'] = resList
#         myclient.close()
#         return Response(res, status=status.HTTP_200_OK)


class newsCrawlerMany(APIView):
    '''
    获取数据源list, 更新数据源爬取进度
    '''
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        global crawler_many_process
        crawler_many_process = 0
        res = {"code": 20000}
        mongo_client = "mongodb://localhost:27017"
        myclient = pymongo.MongoClient(mongo_client)
        dblist = myclient.list_database_names()
        if "cloud_academic" not in dblist:
            raise Exception('cloud_academic数据库不存在')
        mydb = myclient["cloud_academic"]
        xpath_content = mydb['news_xpath']
        strategy_content = mydb['crawler_strategy']
        manage = mydb['news_xpath_manage']
        myquery = {"策略名称": request.GET['strategy_name'], "开始日期": request.GET['beginDate']}
        strategy_info = strategy_content.find_one(myquery)
        column = strategy_info['栏目名称']
        xpathLs = None
        n = 0
        if column != '':
            query = {'column': column}
            xpathLs = xpath_content.find(query)
            n = xpathLs.count()
        resList = []
        specLogList = []
        xpathInfo = processManage(manage)
        log = createLog(strategy_info)
        # urlList = strategy_info['网站url列表'].split(',')
        # for url in urlList:
        #     myquery = {'web_url': url}
        #     x = xpath_content.find_one(myquery)
        #     specLog = createSpecLog(strategy_info, x)
        #     if x['type'] == '0':
        #         resList.append(nextBtn_crawler(x, xpathInfo))
        #     else:
        #         resList.append(moreBtn_crawler(x, xpathInfo))
        #     crawler_many_process = crawler_many_process + 100 / len(urlList)
        #     specLog['num'] = len(urlList)
        #     specLogList.append(specLog)
        cnt = 0
        for x in xpathLs:
            specLog = createSpecLog(strategy_info, x)
            tmpres = None
            try:
                if x['type'] == '0':
                    tmpres = nextBtn_crawler(x, xpathInfo)
                    resList.append(tmpres)
                else:
                    tmpres = moreBtn_crawler(x, xpathInfo)
                    resList.append(tmpres)
            except Exception as e:
                specLog['status'] = '失败'
                print(e)
                print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
                print('wrong on line:' + str(e.__traceback__.tb_lineno))  # 发生异常所在的行数
            crawler_many_process = crawler_many_process + 100 / n
            specLog['num'] = len(tmpres)
            cnt += len(tmpres)
            specLogList.append(specLog)
        log['num'] = cnt
        addCrawlerLog(log, specLogList)
        res['data'] = resList
        myclient.close()
        return Response(res, status=status.HTTP_200_OK)
