from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pymongo
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from utils.db import mongo_client

res = []


def more_crawler(web_url, title_xpath, content_xpath, content_url, time_xpath, writer_xpath, button_xpath, website_name,
                 lang, column, resource_type):
    # 加载启动项
    global res
    res = []
    print('%s 开始爬取: ' % datetime.now() + web_url)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('--ignore-certificate-errors')  # 主要是该条
    option.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=option)
    driver.get(url=web_url)
    # db
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
    #
    # driver.find_elements_by_xpath(time_xpath)[-1].text[0:10] > "2021-01-31"
    # while条件，可设置爬取到具体时间节点，否则会持续到最末
    while True:
        try:
            print('%s %s %s' % (datetime.now(), web_url, '模拟点击获取更多信息中'))
            try:
                element = driver.find_element_by_xpath(button_xpath)
            except:
                break
            temp_title = driver.find_elements_by_xpath(title_xpath)[-1].text
            temp_query = {"title": temp_title}
            if (content.count_documents(temp_query) != 0):
                print('%s %s %s' % (datetime.now(), web_url, '发现重复标题，提前退出'))
                break
        except NoSuchElementException:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, button_xpath)))
            continue
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    flags = {'title': 1, 'writer': 1, 'date': 1, 'content': 1, 'url': 1}
    try:
        title_list = driver.find_elements_by_xpath(title_xpath)
        if (len(title_list) == 0):
            flags['title'] = 0
    except NoSuchElementException:
        flags['title'] = 0
    try:
        writer_list = driver.find_elements_by_xpath(writer_xpath)
        if (len(writer_list) == 0):
            flags['writer'] = 0
    except NoSuchElementException:
        flags['writer'] = 0
    try:
        date_list = driver.find_elements_by_xpath(time_xpath)
        if (len(date_list) == 0):
            flags['date'] = 0
    except NoSuchElementException:
        flags['date'] = 0
    try:
        content_list = driver.find_elements_by_xpath(content_xpath)
        if (len(content_list) == 0):
            flags['content'] = 0
    except NoSuchElementException:
        flags['content'] = 0
    try:
        url_list = driver.find_elements_by_xpath(content_url)
        if (len(url_list) == 0):
            flags['url'] = 0
    except NoSuchElementException:
        flags['url'] = 0
    # 获取元素文本内容
    n = len(title_list)
    try:
        for i in range(len(title_list)):
            if (i % 10 == 0):
                print('%s %s %s %d/%d' % (datetime.now(), web_url, '写入数据库进度:', i, n))
            temp_title = title_list[i].text if flags['title'] == 1 else 'null'
            temp_writer = writer_list[i].text if flags['writer'] == 1 else 'null'
            temp_date = date_list[i].text if flags['date'] == 1 else 'null'
            temp_content = content_list[i].text if flags['content'] == 1 else 'null'
            temp_url = url_list[i].get_attribute('href') if flags['url'] == 1 else 'null'
            filter = {'column_url': web_url,
                      'title': temp_title,
                      'content': temp_content,
                      'url': temp_url,
                      'writer': temp_writer}
            query = {'column_url': web_url,
                     'title': temp_title,
                     'content': temp_content,
                     'time': temp_date,
                     'url': temp_url,
                     'writer': temp_writer,
                     'website_name': website_name,
                     'lang': lang,
                     'column': column,
                     'resource_type': resource_type
                     }
            content.update_one(filter, {'$set': query}, upsert=True)
    except:
        pass

    print('%s %s %s %d' % (datetime.now(), web_url, '爬取数目:', len(title_list)))
    driver.quit()
    temp = content.find({"website_name": website_name, "column": column})
    for x in temp:
        res.append({'website_name': x['website_name'], 'title': x['title'], 'content': x['content'], 'time': x['time'],
                    'url': x['url'], 'writer': x['writer']})
    myclient.close()
    return res


if __name__ == '__main__':

    myclient = pymongo.MongoClient(mongo_client)
    dblist = myclient.list_database_names()
    if "cloud_academic" not in dblist:
        raise Exception('cloud_academic数据库不存在')
    mydb = myclient["cloud_academic"]
    collist = mydb.list_collection_names()
    content = None
    for str in collist:
        if (str == 'news_xpath'):
            xpath = mydb[str]
        else:
            continue
        myquery = {"type": 1}
        myclient.close()
        for x in xpath.find(myquery):
            more_crawler(x['web_url'], x['title_xpath'], x['content_xpath'], x['content_url'],
                         x['time_xpath'], x['writer_xpath'], x['button_xpath'],
                         x['website_name'], x['lang'], x['column'], x['resource_type'])
