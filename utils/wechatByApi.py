# coding: utf-8
import os
from pprint import pprint
from wechatarticles import PublicAccountsWeb
from wechatarticles.utils import save_json
import time
import pymongo
from utils.db import mongo_client
cookie = "appmsglist_action_3888618203=card; pgv_pvi=4391323648; RK=sABV6G9zN3; ptcz=bba395cfe3d5d3892abe4999cb14586aa0d1de3abd0a2c2197c26147cf77b05c; pgv_pvid=5541287920; o_cookie=1009303269; pac_uid=1_1009303269; eas_sid=R156N0v9D9K2M2J726Z2l1p3a7; ied_qq=o1009303269; uin_cookie=o1009303269; LW_uid=G1Q6p1d2L5h0V7Z7k338c4T0Y9; LW_sid=Z186B1Y28581j9K102Y1U7H5a6; ptui_loginuin=1009303269; pt_sms_phone=183******97; iip=0; tvfe_boss_uuid=e00558ce0b96c0b2; ua_id=rddsp4UOT8SM4Mz9AAAAACuRDCOdiHjnpX8aiuXsDHs=; wxuin=19426931639226; openid2ticket_o25rH54xDLEjGbZshR7WpzpOABsM=; mm_lang=zh_CN; uuid=210737f4efcd5d86a9f246f923760e4e; rand_info=CAESIE28I2d4JEvcWJwYxNrGV0/MSMYacquf3x5pEoNeUHcC; slave_bizuin=3888618203; data_bizuin=3888618203; bizuin=3888618203; data_ticket=bELHWOG/w/ZZFFMjj9HJG6ObuI6PJGzJ6ZlQZfxavEyW9gtwqmg4stkKrKBPrSbR; slave_sid=V1BCelJUQTZHTlkzSXd3amZIMjFsS0lWeUlkbkZWZVYzTGZDOEoyck5IbjJOUEtUOGtuaFJvcGlJYzhlSFBDWGNibzJDQkNqbG9oOUxtc1FXQjZLZTd4WGJ5Qm5XWk9Bb1JrOXRiSndlNGtfNzFqTU5sSTlNZlVtNG92Y1pBZ2FoYm03UTFyWVIyMlpja3lx; slave_user=gh_cd39434176bb; xid=2bb70321c9418ac2beaeb5f419c6193b"
token = "108309720"
nickname = "科技美学"
articles_sum = 0
article_data = []
res = []
def timeStampToTimeString(timeStamp):
    timeArray = time.localtime(timeStamp)  # timeStamp_13 / 1000
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def wechatCrawlerByApi(Name):
    global cookie,token,nickname,articles_sum,article_data,res
    res = []
    article_data = []
    nickname = Name
    myclient = pymongo.MongoClient(mongo_client)
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        raise Exception('cloud_academic数据库不存在')
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    content = None
    for str in collist:
        if (str == 'news_content'):
            content = mydb[str]
        else:
            continue
    ###
    paw = PublicAccountsWeb(cookie=cookie, token=token)
    articles_sum = paw.articles_nums(nickname)
    print("articles_sum:", end=" ")
    print(articles_sum)
    print(int(articles_sum/5))
    # official_info = paw.official_info(nickname)
    for i in range(0,int(articles_sum/5),7):
        print("now at:%d"%i)
        temp = paw.get_urls(nickname, begin="%d"%i, count="5")
        for article in temp:
            article['create_time'] = timeStampToTimeString(article['create_time'])
            temp_title = article['title']
            temp_content = article['digest']
            temp_date = article['create_time']
            temp_url = article['link']
            filter = {'website_name': nickname,
                      'title': temp_title,
                      'content': temp_content,
                      'writer': nickname}
            query = {'column_url': '',
                     'title': temp_title,
                     'content': temp_content,
                     'time': temp_date,
                     'url': temp_url,
                     'writer': nickname,
                     'website_name': nickname,
                     'lang': '中',
                     'column': '',
                     'resource_type': ''
                     }
            content.update_one(filter, {'$set': query}, upsert=True)
        article_data.append(temp)
        pprint(temp)
        # article_data.append(temp)
        time.sleep(180)# 访问过快会被ban号

    temp = content.find({"website_name": nickname})
    for x in temp:
        res.append({'website_name': x['website_name'], 'title': x['title'], 'content': x['content'], 'time': x['time'],
                    'url': x['url'], 'writer': x['writer']})
    myclient.close()
    return res
    # print("artcles_data:")
    # print(len(article_data))
    # pprint(article_data)
    # save_json("paw.json", article_data)


if __name__ == "__main__":
    # print(timeStampToTimeString(1619356928))
    wechatCrawlerByApi(nickname)
    # title =[]
    # for i in article_data:
    #     title.append(i['title'])
    # print(title)
    # print(len(article_data))


