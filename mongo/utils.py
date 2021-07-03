import pymongo


def getWebSiteNameList(database):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    res = []
    for str in collist:
        if (str == database):
            mycol = mydb[str]
        else:
            continue

        res = mycol.distinct('website_name')
        myclient.close()
        return res


def getColumnList(database, website_name):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        print("数据库不存在！")
        return 0
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    res = []
    for str in collist:
        if (str == database):
            mycol = mydb[str]
        else:
            continue
        res = mycol.find({"website_name": website_name}).distinct('column')
        # print(res)
        myclient.close()
        return res


def getXpathValueList(valuename):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["cloud_academic"]
    mycol = mydb["news_xpath"]
    ls = []
    for x in mycol.find():
        ls.append(x[valuename])
    return ls
