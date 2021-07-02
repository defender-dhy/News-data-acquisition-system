from utils.db import mongo_client
import pymongo


def addNewStrategy(strategy):
    try:
        filter = {'策略名称': strategy['name'], '开始日期': strategy['beginDate']}
        query = {'策略名称': strategy['name'], '开始日期': strategy['beginDate'], '开始时间': strategy['beginTime'],
                 '结束时间': strategy['endTime'], '网站url列表': strategy['urlList'].split(','), '爬虫频率': strategy['freq'],
                 '频率类型': strategy['freqType'], '范围类型': ''}
        myclient = pymongo.MongoClient(mongo_client)
        mydb = myclient['cloud_academic']
        content = mydb['crawler_strategy']
        content.update_one(filter, {'$set': query}, upsert=True)
        return 1
    except:
        return 0
