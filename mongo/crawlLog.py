from utils.db import mongo_client
import pymongo
import json


def getAllCrawlerLog(filter):
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['crawler_log']
    ls = []
    for c in content.find():
        dic = {'beginDate': c['开始日期'], 'beginTime': c['开始时间'], 'endTime': '结束时间',
               'mode': c['模式'], 'urlList': c['网站url列表'], 'strategyName': c['策略名称'], 'num': c['爬取数量'],
               'detail': c['详情说明']}
        ls.append(dic)
    return ls


def getAllSpecCrawlerLog(rawfilter):
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    content = mydb['crawler_spec_log']
    ls = []
    findCont = None
    if rawfilter == '':
        findCont = content.find()
    else:
        filter = {}
        rawfilter = json.loads(rawfilter)
        filter['开始日期'] = rawfilter['beginDate']
        filter['开始时间'] = rawfilter['beginTime']
        findCont = content.find(filter)
    for c in findCont:
        dic = {'beginDate': c['开始日期'], 'beginTime': c['开始时间'], 'endTime': '结束时间',
               'mode': c['模式'], 'num': c['数据量'], 'detail': c['备注'],
               'status': c['状态'], 'column': c['栏目名称'], 'websiteName': c['网站名称']}
        ls.append(dic)
    return ls


def addCrawlerLog(log, speclogList):
    filter = {'开始日期': log['beginDate'], '开始时间': log['beginTime']}
    query = {'策略名称': log['name'], '开始日期': log['beginDate'], '开始时间': log['beginTime'],
             '结束时间': log['endTime'], '网站url列表': log['urlList'], '模式': log['mode'], '爬取数量': log['num'],
             '详情说明': ''}
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient['cloud_academic']
    logSheet = mydb['crawler_log']
    specLogSheet = mydb['crawler_spec_log']
    logSheet.update_one(filter, {'$set': query}, upsert=True)
    for l in speclogList:
        filter = {'开始日期': l['beginDate'], '开始时间': l['beginTime']}
        query = {'开始日期': l['beginDate'], '开始时间': l['beginTime'],
                 '结束时间': l['endTime'], '模式': l['mode'], '网站名称': l['urlName'],
                 '状态': l['status'], '数据量': l['num'], '栏目名称': l['column'], '备注': ''}
        specLogSheet.update_one(filter, {'$set': query}, upsert=True)
    return


def createSpecLog(strategy_info, xpath_info):
    specLog = {'beginDate': strategy_info['开始日期'], 'beginTime': strategy_info['开始时间'], 'endTime': strategy_info['结束时间'],
               'mode': '自动', 'urlName': xpath_info['website_name'], 'column': xpath_info['website_name'],
               'status': '成功', 'num': 0}
    return specLog


def createLog(strategy_info):
    log = {'name': strategy_info['策略名称'], 'beginDate': strategy_info['开始日期'], 'beginTime': strategy_info['开始时间'],
           'endTime': strategy_info['结束时间'], 'urlList': strategy_info['网站url列表'], 'mode': '自动', 'num': 0}
    return log


def modifyLogDetail(log):
    try:
        filter = {'开始日期': log['beginDate'], '开始时间': log['beginTime']}
        query = {'策略名称': log['name'], '开始日期': log['beginDate'], '开始时间': log['beginTime'],
                 '结束时间': log['endTime'], '网站url列表': log['urlList'], '模式': log['mode'], '爬取数量': log['num'],
                 '详情说明': log['detail']}
        myclient = pymongo.MongoClient(mongo_client)
        mydb = myclient['cloud_academic']
        logSheet = mydb['crawler_log']
        logSheet.update_one(filter, {'$set': query}, upsert=True)
        return 1
    except:
        print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
        print(e)
        return 0

# def modifySpecLogDetail(log):
#     filter = {'开始日期': log['beginDate'], '开始时间': log['beginTime']}
#     query = {'策略名称': log['name'], '开始日期': log['beginDate'], '开始时间': log['beginTime'],
#              '结束时间': log['endTime'], '网站url列表': log['urlList'], '模式': log['mode'], '爬取数量': log['num'],
#              '详情说明': log['detail']}
#     myclient = pymongo.MongoClient(mongo_client)
#     mydb = myclient['cloud_academic']
#     logSheet = mydb['crawler_log']
#     logSheet.update_one(filter, {'$set': query}, upsert=True)
