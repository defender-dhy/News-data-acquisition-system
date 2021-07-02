from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pymongo
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from utils.db import mongo_client
import requests
from lxml import etree
from utils.specCrawler import getSpecTree
from utils.specCrawler import getSpecContent

res = []


def moreBtn_crawler(x, xpathInfo):
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
    cnt = 0
    while True:
        try:
            print('%s %s %s' % (datetime.now(), x['web_url'], '模拟点击获取更多信息中'))
            try:
                element = driver.find_element_by_xpath(x['button_xpath'])
            except:
                break
            # print(driver.find_elements_by_xpath(x['title_xpath']))
            temp_title = driver.find_elements_by_xpath(x['title_xpath'])[-1].text
            temp_query = {"title": temp_title}
            if content.count_documents(temp_query) != 0:
                print('%s %s %s' % (datetime.now(), x['web_url'], '发现重复标题，提前退出'))
                break
        except NoSuchElementException:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, x['button_xpath'])))
            continue
        try:
            try:
                driver.execute_script("arguments[0].click();", element)
            except:
                element.click()
        except:
            break
        time.sleep(1)
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
    try:
        for i in range(n):
            filter = {'column_url': x['web_url'],
                      'title': dataLsDict['title_xpath'][i].text
                      if flagDict['title_xpath'] == 1 else 'null',
                      'url': dataLsDict['content_url'][i].get_attribute('href')
                      if flagDict['content_url'] == 1 else 'null'}
            query = {}
            tree = getSpecTree(dataLsDict['content_url'][i].get_attribute('href'))
            # specdriver.find_elements_by_xpath(x['content_url'])[i].click()
            # print(x.keys())
            for key in x.keys():
                if key not in xpathInfo.keys():
                    continue
                t = xpathInfo[key]['crawler']
                try:
                    if xpathInfo[key]['saveName'] is None:
                        continue
                    if t == '1':
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
                    continues
            cnt += 1
            if cnt % 10 == 0:
                print('%s %s %s %d' % (datetime.now(), x['web_url'], '写入数据库进度:', cnt))
            content.update_one(filter, {'$set': query}, upsert=True)
            # specdriver.back()
    except Exception as e:
        print('Exception 1')
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
    print('%s %s %s %d' % (datetime.now(), x['web_url'], '爬取数目:', len(dataLsDict['title_xpath'])))
    driver.quit()
    temp = content.find({"website_name": x['website_name'], "column": x['column']})
    for x in temp:
        res.append({'website_name': x['website_name'], 'title': x['title'], 'content': x['content'], 'time': x['time'],
                    'url': x['url'], 'writer': x['writer']})
    myclient.close()
    return res
