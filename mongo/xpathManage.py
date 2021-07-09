from utils.db import mongo_client
import pymongo
import json
import pandas as pd


def getXpathManage():
    try:
        myclient = pymongo.MongoClient(mongo_client)
        mydb = myclient['cloud_academic']
        content = mydb['news_xpath_manage']
        res = []
        for c in content.find():
            cd = {'type': c['类型'], 'inSpec': c['是否在详情页'], 'saveName': c['数据库存储名字'],
                  'needCrawl': c['需要爬取'], 'needSave': c['需要存储'], 'EnglishName': c['字段名称英'], 'ChineseName': c['字段名称中']}
            res.append(cd)
        return res
    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
        print(e)
        return []


def postXpathManage(cont):
    try:
        # print(cont)
        # cont.replace('null', 'None')
        cont = json.loads(cont)
        # cont = eval(cont.strip())
        # print(cont['EnglishName'])
        filter = {'字段名称英': cont['EnglishName']}
        query = {'字段名称英': cont['EnglishName'], '字段名称中': cont['ChineseName'], '是否在详情页': cont['inSpec'],
                 '需要爬取': cont['needCrawl'], '数据库存储名字': cont['saveName'], '类型': cont['type'], '需要存储': cont['needSave']}
        myclient = pymongo.MongoClient(mongo_client)
        mydb = myclient['cloud_academic']
        content = mydb['news_xpath_manage']
        content.update_one(filter, {'$set': query}, upsert=True)
        return 1
    except Exception as e:
        print('fail')
        print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
        print(e)
        return 0


def getXpathList(query):
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['news_xpath']
    res = []
    if query is None:
        for c in content.find():
            cd = {}
            for k in c.keys():
                cd[k] = c[k]
            res.append(cd)
    else:
        for c in content.find(query):
            cd = {}
            for k in c.keys():
                cd[k] = c[k]
            res.append(cd)
    return res


def modifyXpath(rawfilterLs, rawqueryLs):
    try:
        myclient = pymongo.MongoClient(mongo_client)
        mydb = myclient['cloud_academic']
        content = mydb['news_xpath']
        for i in range(len(rawfilterLs)):
            filter = {}
            query = {}
            for k in rawfilterLs[i].keys():
                filter[k] = rawfilter[k]
            for k in rawqueryLs[i].keys():
                query[k] = rawquery[k]
            content.update_one(filter, {'$set': query}, upsert=True)
        return 1
    except Exception as e:
        print(e)


def modifyOneXpath(cont):
    try:
        myclient = pymongo.MongoClient(mongo_client)
        mydb = myclient['cloud_academic']
        content = mydb['news_xpath']
        cont = json.loads(cont)
        filter = {'web_url': cont['web_url']}
        del cont['_id']
        content.update_one(filter, {'$set': cont}, upsert=True)
        return 1
    except Exception as e:
        print(e)
        return 0


def addXpathByFile(file):
    # if not os.path.exists('./crawler'):
    #     os.makedirs(settings.UPLOAD_ROOT)
    try:
        if file is None:
            return HttpResponse('请选择要上传的文件')
        temp_save_src = './crawler' + "/" + file.name
        # 循环二进制写入
        with open(temp_save_src, 'wb') as f:
            for i in file.readlines():
                f.write(i)
    except Exception as e:
        return HttpResponse(e)
    df = pd.read_excel(temp_save_src)
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['news_xpath']
    content.insert(json.loads(df.T.to_json()).values())

