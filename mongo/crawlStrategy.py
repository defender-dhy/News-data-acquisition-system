from utils.db import mongo_client
import pymongo
import json


def addNewStrategy(strategy):
    try:
        print(strategy)
        strategy = json.loads(strategy)
        filter = {'策略名称': strategy['name'], '开始日期': strategy['beginDate']}
        query = {'策略名称': strategy['name'], '开始日期': strategy['beginDate'], '开始时间': strategy['beginTime'],
                 '结束时间': strategy['endTime'], '网站url列表': strategy['urlList'], '爬虫频率': strategy['freq'],
                 '频率类型': strategy['freqType'], '范围类型': '', '栏目名称': strategy['column'],
                 '开始日期类型': strategy['beginDateType'], '开始时间类型': strategy['beginTimeType'],
                 '结束时间类型': strategy['endTimeType']}
        myclient = pymongo.MongoClient(mongo_client)
        mydb = myclient['cloud_academic']
        content = mydb['crawler_strategy']
        content.update_one(filter, {'$set': query}, upsert=True)
        return 1
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
        return 0


def getStrategyNameList():
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['crawler_strategy']
    nameLs = []
    for c in content.find():
        nameLs.append(c['策略名称'])
    return nameLs


def getStrategyBeginDateList():
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['crawler_strategy']
    nameLs = []
    for c in content.find():
        nameLs.append(c['开始日期'])
    return nameLs


def getAllStrategyLs():
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['crawler_strategy']
    strategyLs = []
    for c in content.find():
        strategyLs.append({'beginDate': c['开始日期'], 'beginTime': c['开始时间'], 'endTime': '结束时间', 'name': c['策略名称'],
                           'freq': c['爬虫频率'], 'column': c['栏目名称']})
    return strategyLs
