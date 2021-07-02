from utils.db import mongo_client
import pymongo


def getXpathManage():
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['news_xpath_manage']
    res = []
    for c in content.find():
        cd = {}
        for k in c.keys():
            if k != '_id':
                cd[k] = c[k]
        res.append(cd)
    return res


def postXpathManage(cont):
    try:
        filter = {'字段名称英': cont['English_name']}
        query = {'字段名称英': cont['English_name'], '字段名称中': cont['Chinese_name'], '是否在详情页': cont['inSpec'],
                 '需要爬取': cont['needCrawler'], '数据库存储名字': cont['savaName'], '类型': cont['type']}
        mydb = myclient['cloud_academic']
        content = mydb['news_xpath_manage']
        content.update_one(filter, {'$set': query}, upsert=True)
        return 1
    except Exception as e:
        print(e)
    finally:
        return 0


def getXpathList(query):
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['news_xpath']
    res = []
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
    finally:
        return 0
