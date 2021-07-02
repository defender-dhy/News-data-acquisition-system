from selenium import webdriver
import time
import pymongo
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from utils.db import mongo_client
from lxml import etree
import requests
import json
from utils.specCrawler import getSpecTree
from utils.specCrawler import getSpecContent

res = []


def processManage(manage):
    dic = {}
    for m in manage.find():
        dic[m['字段名称英']] = {'crawler': m['需要爬取'], 'spec': m['是否在详情页'], 'saveName': m['数据库存储名字'], 'needSave': m['需要存储']}
    return dic


def nextBtn_crawler(x, xpathInfo):
    print('%s 开始爬取: ' % datetime.now() + x['web_url'])
    option = webdriver.ChromeOptions()
    option.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    option.add_argument('headless')
    option.add_argument('--ignore-certificate-errors')  # 主要是该条
    option.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=option)
    # specdriver = webdriver.Chrome(options=option)
    driver.get(url=x['web_url'])
    myclient = pymongo.MongoClient(mongo_client)
    mydb = myclient["cloud_academic"]
    content = mydb['news_content']
    res = []
    dataLsDict = {}
    flagDict = {}
    second = 0
    if second == 1:
        try:
            title_list = driver.find_elements_by_xpath(x['title_xpath'])
            temp_title = title_list[0].text
            temp_query = {"title": temp_title}
            if content.count_documents(temp_query) != 0:
                print('%s %s %s' % (datetime.now(), x['web_url'], '发现重复标题，提前退出'))
                return res
        except Exception as e:
            print('Exception 0')
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print('wrong on line:' + str(e.__traceback__.tb_lineno))  # 发生异常所在的行数
            return res
    cnt = 0
    url_ls = []
    title_ls = []
    while True:
        first_title = driver.find_element_by_xpath(x['title_xpath']).text
        if first_title in title_ls:
            break
        else:
            title_ls.append(first_title)
        for key in x.keys():
            if key not in xpathInfo.keys():
                continue
            t = xpathInfo[key]['crawler']
            if t == '1':
                try:
                    ls = driver.find_elements_by_xpath(x[key])
                    if len(ls) == 0:
                        flagDict[key] = 0
                    else:
                        flagDict[key] = 1
                    dataLsDict[key] = ls
                except:
                    dataLsDict[key] = []
                    flagDict[key] = 0
        n = len(dataLsDict['title_xpath'])
        # temp_query = {"title": dataLsDict['title_xpath'][0].text}
        # if content.count_documents(temp_query) != 0:
        #     print('%s %s %s' % (datetime.now(), x['web_url'], '发现重复标题，提前退出'))
        #     break
        # print(n)
        try:
            for i in range(n):
                filter = {'column_url': x['web_url'],
                          'title': dataLsDict['title_xpath'][i].text
                          if flagDict['title_xpath'] == 1 else 'null',
                          'url': dataLsDict['content_url'][i].get_attribute('href')
                          if flagDict['content_url'] == 1 else 'null'}
                query = {}
                tree = getSpecTree(dataLsDict['content_url'][i].get_attribute('href'))
                for key in x.keys():
                    if key not in xpathInfo.keys():
                        continue
                    t = xpathInfo[key]['crawler']
                    try:
                        if xpathInfo[key]['needSave'] == '0':
                            continue
                        if t == '1':
                            # if key == 'writer_xpath':
                            #     print('writer_xpath')
                            #     print(xpathInfo[key]['saveName'])
                            #     print(dataLsDict[key][i].text)
                            if key == 'content_url':
                                query[xpathInfo[key]['saveName']] = dataLsDict[key][i].get_attribute('href')
                            else:
                                query[xpathInfo[key]['saveName']] = dataLsDict[key][i].text
                        elif t == '2':
                            # query[xpathInfo[key]['saveName']] = getSpecContentDriver(specdriver, x[key], key)
                            query[xpathInfo[key]['saveName']] = getSpecContent(tree, x[key], key)
                        else:
                            query[xpathInfo[key]['saveName']] = x[key]
                    except:
                        query[xpathInfo[key]['saveName']] = ''
                        continue
                cnt += 1
                if cnt % 10 == 0:
                    print('%s %s %s %d' % (datetime.now(), x['web_url'], '写入数据库进度:', cnt))
                content.update_one(filter, {'$set': query}, upsert=True)
        except Exception as e:
            print('Exception 1')
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print('wrong on line:' + str(e.__traceback__.tb_lineno))  # 发生异常所在的行数
            print()
        try:
            try:
                element = driver.find_element_by_xpath(x['button_xpath'])
            except:
                element = driver.find_element_by_xpath(x['button1_xpath'])
            try:
                element.click()
            except:
                driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
            # WebDriverWait(driver, timeout=15).until(
            #     lambda driver: driver.execute_script('return document.readyState === "complete"')
            # )
            # print(driver.execute_script('return document.readyState'))
        except Exception as e:
            print('Exception 2')
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print('wrong on line:' + str(e.__traceback__.tb_lineno) + '\n')  # 发生异常所在的行数
            break
    print('%s %s %s %d' % (datetime.now(), x['web_url'], '爬取数目:', cnt))
    driver.quit()
    temp = content.find({"website_name": x['website_name'], "column": x['column']})
    for x in temp:
        res.append({'website_name': x['website_name'], 'title': x['title'], 'content': x['content'], 'time': x['time'],
                    'url': x['url'], 'writer': x['writer']})
    myclient.close()
    return res
